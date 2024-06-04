import struct
import os

def read_bytes(file, size):
    data = file.read(size)
    if len(data) != size:
        raise IOError("Unexpected end of file")
    return data

#We read integer using this function
def read_uint32(file):
    return struct.unpack('<I', read_bytes(file, 4))[0]
#Even if there’s only one value to unpack, it will still be returned as a single-element tuple.

#we expect an unsigned 16-bit integer (2 bytes)
def read_uint16(file):
    return struct.unpack('<H', read_bytes(file, 2))[0]

def extract_zip(file_path, output_dir):
    with open(file_path, 'rb') as file:
        file.seek(-22, os.SEEK_END)  # Start by searching for the End of Central Directory record
        #The file.seek(offset, whence) method in Python is used to move the file pointer (cursor) to a specific position within the file
        #seeks to a position 22 bytes before the end of the file.


        #The EOCD record contains essential information about the ZIP archive, including the number of entries,
        #  the central directory offset, and other metadata.
        eocd = file.read(22)
        
        if eocd[0:4] != b'PK\x05\x06':  # EOCD signature
            raise ValueError("Not a ZIP file")

#Size of central directory in bytes
        central_directory_size = struct.unpack('<I', eocd[12:16])[0]

# Offset to start of central directory
        central_directory_offset = struct.unpack('<I', eocd[16:20])[0]

        file.seek(central_directory_offset)
        entries = []


#The loop processes each central directory file header.
        while file.tell() < central_directory_offset + central_directory_size:
            #The tell() method returns the current file position in a file stream.
            header = file.read(46)
            if header[0:4] != b'PK\x01\x02':  # Central Directory File Header signature
                raise ValueError("Malformed Central Directory File Header")

            compressed_size = struct.unpack('<I', header[20:24])[0]
            uncompressed_size = struct.unpack('<I', header[24:28])[0]
            file_name_length = struct.unpack('<H', header[28:30])[0]
            extra_field_length = struct.unpack('<H', header[30:32])[0]
            file_comment_length = struct.unpack('<H', header[32:34])[0]
            local_header_offset = struct.unpack('<I', header[42:46])[0]

            file_name = read_bytes(file, file_name_length).decode()
            file.seek(extra_field_length + file_comment_length, os.SEEK_CUR)

            entries.append((file_name, local_header_offset, compressed_size, uncompressed_size))

        for entry in entries:
            file_name, local_header_offset, compressed_size, uncompressed_size = entry

            file.seek(local_header_offset)
            local_header = file.read(30)
            if local_header[0:4] != b'PK\x03\x04':  # Local file header signature
                raise ValueError("Malformed Local File Header")

            file_name_length = struct.unpack('<H', local_header[26:28])[0]
            extra_field_length = struct.unpack('<H', local_header[28:30])[0]

            file.seek(file_name_length + extra_field_length, os.SEEK_CUR)

            output_file_path = os.path.join(output_dir, file_name)
            os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

            with open(output_file_path, 'wb') as output_file:
                output_file.write(read_bytes(file, compressed_size))


extract_zip('HISTDATA_COM_XLSX_EURUSD_M12018.zip', 'output_directory')
