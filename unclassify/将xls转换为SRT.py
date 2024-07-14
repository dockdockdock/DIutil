import pandas as pd
import sys, os
import xlrd

def timecode_to_srt(timecode):
    """Convert timecode from 'HH:MM:SS:FF' to 'HH:MM:SS,MS'."""
    # Assuming a frame rate of 24 fps for conversion
    hours, minutes, seconds, frames = map(int, timecode.split(':'))
    milliseconds = int((frames / 24) * 1000)
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"

def process_xls(xls_file_path):
    """Load and clean data from an XLS file using xlrd."""
    data = pd.read_excel(xls_file_path, engine='xlrd', header=0, names=['Thumbnail','id','in','out','dur', 'content'])
    # Convert 'Start' and 'End' columns to string to handle unexpected data types
    data = data.drop(columns=['Thumbnail', 'dur', 'content'])
    data['in'] = data['in'].astype(str)
    data['out'] = data['out'].astype(str)
    return data

def convert_to_srt(data, srt_file_path):
    print(type(data))  # 应输出 <class 'pandas.core.frame.DataFrame'>
    # Generate SRT content
    srt_data = []
    for I, row in data.iterrows():
        start_srt = timecode_to_srt(row['in'])  # 使用 'in'
        end_srt = timecode_to_srt(row['out'])   # 使用 'out'
        srt_data.append(f"{I+1}")
        srt_data.append(f"{start_srt} --> {end_srt}")
        srt_data.append(row['id'])  # 假设您使用 'id' 作为占位符
        srt_data.append("")  # Empty line after each subtitle entry
    
    srt_content = "\n".join(srt_data)
    # Write to an SRT file
    with open(srt_file_path, 'w') as file:
        file.write(srt_content)
    
    srt_content = "\n".join(srt_data)
    
    # Write to an SRT file
    with open(srt_file_path, 'w') as file:
        file.write(srt_content)

def main():
    if len(sys.argv) < 2:
        print("Usage: python script_name.py <input_xls_file>")
        sys.exit(1)

    xls_file_path = sys.argv[1]
    output_dir = os.path.dirname(xls_file_path)  # Get the directory of the input file

    # Ensure the directory exists, although it should since the input file is there
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Construct the output file path using the same directory as the input file
    output_file_name = os.path.splitext(os.path.basename(xls_file_path))[0] + ".srt"
    output_file = os.path.join(output_dir, output_file_name)
    
    data = process_xls(xls_file_path)
    convert_to_srt(data, output_file)
    print(f"SRT file created at {output_file}")

if __name__ == "__main__":
    main()