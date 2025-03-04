# Rename Movie

This Python script automates the process of renaming files in the current directory by standardizing their filenames. The script performs the following operations on each filename:

- Replaces periods (`.`) with spaces (` `), except for the file extension separator.
- Removes parentheses `(` and `)`.
- Eliminates specific digit sequences (`1080` and `2160`).
- Identifies four consecutive digits representing a year and encloses them in parentheses.
- Truncates any characters following the identified year, preserving the file extension.

## Features

- **Batch Processing**: Automatically processes all files in the current directory.
- **Filename Standardization**: Cleans and formats filenames to a consistent structure.
- **Year Identification**: Detects year patterns within filenames and formats them appropriately.

## Requirements

- **Python 3.x**

## Usage

1. **Prepare the Script**: Save the provided script to a `.py` file in the directory containing the files you wish to rename.

2. **Run the Script**: Execute the script using a terminal or command prompt:

   ```bash
   python script_name.py
   ```

3. **Processing**: The script will process each file in the current directory, rename it according to the defined rules, and display the renaming actions performed.

### Example

**Before Running the Script**:

```
My.Movie.Title.1080p.(2021).mkv
Another.Movie.Title.2160p.(2019).mp4
Sample.Movie.Title.2020.mkv
```

**After Running the Script**:

```
My Movie Title (2021).mkv
Another Movie Title (2019).mp4
Sample Movie Title (2020).mkv
```

## Functions

- `process_filename(filename)`: Processes an individual filename by applying the renaming rules and returns the new filename.

- `rename_files_in_directory()`: Iterates over all files in the current directory, applies the `process_filename` function, and renames the files accordingly.

## Notes

- **Backup**: It's recommended to back up your files before running the script to prevent any unintended data loss.

- **Customization**: You can modify the script to adjust the renaming rules according to your specific requirements.

- **File Extensions**: The script preserves the original file extensions during the renaming process.

## License

This project is licensed under the MIT License.

## References

- [Renaming multiple files using Python](https://www.geeksforgeeks.org/rename-multiple-files-using-python/)
- [Python os.rename() Method](https://www.tutorialspoint.com/python/os_rename.htm)
- [Automate Renaming Files with Python - YouTube](https://www.youtube.com/watch?v=xRMpit-xEaI)

For further information on automating file renaming with Python, consider exploring the [Python Tutorial: Automate Parsing and Renaming of Multiple Files](https://www.youtube.com/watch?v=ve2pmm5JqmI) video. 
