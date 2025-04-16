# Filename: generate_puzzle_table.py
import os
import re
from pathlib import Path
from collections import defaultdict
import pandas as pd  # Added for Excel reading
from datetime import datetime # Added for date parsing

# --- Configuration ---
POSTS_DIR = Path("_posts/results")
EXCEL_FILE = Path("_posts/UnEvapuzzles/data.xlsx") # Path to the Excel file
OUTPUT_FILE = Path("_includes/puzzle_list_table.html")
# --- End Configuration ---

def parse_excel_datetime(dt):
    """Handles parsing datetime objects or strings from Excel."""
    if isinstance(dt, datetime):
        return dt
    try:
        # Try parsing common string formats if not already datetime
        return pd.to_datetime(dt)
    except Exception:
        return None

def extract_data_from_file(filepath):
    """
    Extracts Puzzle ID, Submission/Deadline, PDB ID, and Reference from a single Markdown file.
    """
    puzzle_id = None
    puzzle_num = None
    submission_deadline = ""
    pdb_id = ""
    reference = ""
    detail_url = ""
    assessment_url = ""

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            in_front_matter = False
            file_content = f.read()
            lines = file_content.splitlines()

            date_str = ""
            for i, line in enumerate(lines):
                line = line.strip()
                if i == 0 and line == '---':
                    in_front_matter = True
                    continue
                if in_front_matter:
                    if line == '---':
                        in_front_matter = False
                        break
                    if line.startswith('title:'):
                        title_content = line.split(':', 1)[-1].strip().strip('"')
                        puzzle_id = title_content
                        num_match = re.search(r'\d+', title_content)
                        if num_match:
                            puzzle_num = num_match.group()
                    elif line.startswith('date:'):
                        date_str = line.split(':', 1)[-1].strip()
                        date_match = re.search(r'(\d{4})-(\d{2})-(\d{2})', date_str)
                        if date_match:
                            year, month, day = date_match.groups()
                            detail_url = f"/results/{year}/{month}/{day}/"

            pdb_match = re.search(r'\*\*PDB id\*\*\s*:\s*\[(.*?)\]', file_content)
            if pdb_match:
                pdb_id = pdb_match.group(1).strip()

            submission_match1 = re.search(r'\*\*Puzzle Submission/Deadline:\*\*\s*([\d\.\/]+)', file_content)
            submission_match2 = re.search(r'\*\*Puzzle Submission/Deadline:\*\*.*?([\d]{4}\.[\d]{2}\.[\d]{2}/[\d]{2}\.[\d]{2})', file_content)
            submission_match3 = re.search(r'Submission/Deadline.*?([\d]{4}\.[\d]{2}\.[\d]{2}/[\d]{2}\.[\d]{2})', file_content)

            if submission_match1:
                submission_deadline = submission_match1.group(1).strip()
            elif submission_match2:
                submission_deadline = submission_match2.group(1).strip()
            elif submission_match3:
                submission_deadline = submission_match3.group(1).strip()

            if not submission_deadline:
                date_anywhere = re.findall(r'(\d{4}\.\d{2}\.\d{2}/\d{2}\.\d{2})', file_content)
                if date_anywhere:
                    submission_deadline = date_anywhere[0]

            reference_match = re.search(r'\*\*Reference\*\*:?\s*(.*?)(?:\*\*|\n\n|\Z)', file_content, re.DOTALL)
            if reference_match:
                ref_text = reference_match.group(1).strip()
                url_match = re.search(r'\[(.*?)\]\((.*?)\)', ref_text)
                if url_match:
                    ref_text_clean = url_match.group(1).strip()
                    ref_url = url_match.group(2).strip()
                    reference = f"<a href='{ref_url}' target='_blank'>{ref_text_clean}</a>"
                else:
                    reference = ref_text

        if puzzle_id is None:
            print(f"Warning: Could not extract Puzzle ID from title in {filepath.name}")
            match = re.search(r'PZ(\d+)', filepath.stem, re.IGNORECASE)
            if match:
                puzzle_id = f"Puzzle {match.group(1)}"
                puzzle_num = match.group(1)
            else:
                puzzle_id = filepath.stem
                puzzle_num = ""

        num_match = re.search(r'\d+', puzzle_id)
        sort_key = int(num_match.group()) if num_match else 9999

        pz_match = re.search(r'PZ\d+', filepath.stem, re.IGNORECASE)
        if pz_match:
            if detail_url:
                detail_url += f"{pz_match.group()}.html"
            else:
                print(f"Warning: Could not determine date for detail URL of {filepath.name}")
                detail_url = "#"
        else:
            name_part = filepath.stem
            if '-' in name_part:
                name_part = name_part.split('-', 3)[-1] if len(name_part.split('-')) > 3 else name_part
            if detail_url:
                detail_url += f"{name_part}.html"
            else:
                print(f"Warning: Could not determine date for detail URL of {filepath.name}")
                detail_url = "#"

        if puzzle_num:
            assessment_url = f"/table/2000/01/01/PZ{puzzle_num}-3d.html"
        else:
            if pz_match:
                assessment_url = f"/table/2000/01/01/{pz_match.group()}-3d.html"
            else:
                assessment_url = ""

        return {
            "id": puzzle_id,
            "dates": submission_deadline,
            "pdb_id": pdb_id,
            "reference": reference,
            "sort_key": sort_key,
            "detail_url": detail_url,
            "assessment_url": assessment_url,
            "source": "markdown" # Mark the source
        }

    except Exception as e:
        print(f"Error processing file {filepath}: {e}")
        return None

def extract_data_from_excel(filepath):
    """
    Extracts puzzle data from the specified Excel file, formatting dates and IDs.
    """
    excel_data = []
    try:
        df = pd.read_excel(filepath)
        print(f"\nProcessing Excel file: {filepath}")
        print(f"Found columns: {df.columns.tolist()}") # Debug: show columns found

        # --- Adapt these column names based on your actual Excel file ---
        puzzle_col = 'puzzle-name'
        open_col = 'open-time'
        close_col = 'close-time'
        # --- End Adapt ---

        # Check if necessary columns exist
        required_cols = [puzzle_col, open_col, close_col]
        if not all(col in df.columns for col in required_cols):
            print(f"Error: Missing required columns in Excel file. Needed: {required_cols}")
            return []

        for index, row in df.iterrows():
            puzzle_id_raw = str(row[puzzle_col]).strip() if pd.notna(row[puzzle_col]) else ""
            open_time_raw = row[open_col]
            close_time_raw = row[close_col]

            if not puzzle_id_raw:
                continue # Skip rows without a puzzle ID

            # -- Format Puzzle ID --
            puzzle_id_display = puzzle_id_raw # Default to raw ID
            pz_match = re.match(r'PZ(\d+)', puzzle_id_raw, re.IGNORECASE)
            if pz_match:
                puzzle_num = pz_match.group(1)
                puzzle_id_display = f"Puzzle {puzzle_num}" # Format as "Puzzle XX"
            else:
                 puzzle_num = None # Ensure puzzle_num is None if format is unexpected

            # -- Format Dates --
            open_dt = parse_excel_datetime(open_time_raw)
            close_dt = parse_excel_datetime(close_time_raw)

            open_date_str_full = open_dt.strftime('%Y.%m.%d') if open_dt else ""
            # close_date_str_short = close_dt.strftime('%m.%d') if close_dt else "" # Original incorrect approach
            
            # Corrected approach for close date format
            close_date_str_short = ""
            if close_dt:
                # Check if open date is available and years match
                if open_dt and open_dt.year == close_dt.year:
                    close_date_str_short = close_dt.strftime('%m.%d')
                else: # If years don't match or open_dt is missing, use full close date for clarity
                    close_date_str_short = close_dt.strftime('%Y.%m.%d')


            submission_deadline = f"{open_date_str_full}/{close_date_str_short}" if open_date_str_full and close_date_str_short else ""

            # --- Sort Key Extraction ---
            # Use puzzle_num if available, otherwise try extracting digits from raw ID
            if puzzle_num:
                 sort_key = int(puzzle_num)
            else:
                 num_match_sort = re.search(r'\d+', puzzle_id_raw)
                 sort_key = int(num_match_sort.group()) if num_match_sort else 9999

            print(f"  Extracted Excel row: ID='{puzzle_id_display}', Dates='{submission_deadline}'")

            excel_data.append({
                "id": puzzle_id_display, # Use the formatted ID for display
                "dates": submission_deadline,
                "pdb_id": "",
                "reference": "",
                "sort_key": sort_key,
                "detail_url": "#",
                "assessment_url": "",
                "source": "excel"
            })
    except FileNotFoundError:
        print(f"Warning: Excel file not found at {filepath}")
    except Exception as e:
        print(f"Error reading or processing Excel file {filepath}: {e}")
    return excel_data

def generate_html_table(data):
    """
    Generates the HTML table string allowing content wrapping.
    """
    # Sort data by numeric part of Puzzle ID
    sorted_data = sorted(data, key=lambda x: x.get('sort_key', 9999))

    # Start building the HTML table rows
    table_rows_html = ""
    for item in sorted_data:
        pdb_link = ""
        if item.get('pdb_id', ''): # Use .get for safety
            pdb_link = f"<a href='https://www.rcsb.org/structure/{item['pdb_id']}' target='_blank'>{item['pdb_id']}</a>"

        # Wrap puzzle ID in a link ONLY if it's not from Excel (or has a valid URL)
        puzzle_id_display = item['id']
        if item.get('source') == 'markdown' and item.get('detail_url', '#') != '#':
             puzzle_id_display = f"<a href='{item['detail_url']}'>{item['id']}</a>"
        elif item.get('source') == 'excel':
             # Excel entries are not linked (or link to '#')
             puzzle_id_display = item['id'] # Just display the text

        reference_content = item.get('reference', '') # Use .get for safety

        table_rows_html += f"""<tr>
<td class="puzzle-id">{puzzle_id_display}</td>
<td class="submission-date">{item.get('dates', '')}</td>
<td class="pdb-id">{pdb_link}</td>
<td class="reference">{reference_content}</td>
</tr>
"""

    # Generate the complete HTML with wrapping enabled
    html_content = f"""
<script src="/javascripts/sorttable.js"></script>
<script>
    window.onload = function() {{
        // Optional: Decide if default sorting is still needed
        // (document.getElementsByTagName( 'th' )[1]).click();
    }};
</script>
<br/>
<div class="table-container">
<div class="table-header">
Please click the column headers to sort data.
</div>
<div class="table-responsive">
<table class="sortable puzzle-table" border=1>
<thead>
<tr>
<th class="puzzle-id">Puzzle ID</th>
<th class="submission-date">Entry/Expiration</th>
<th class="pdb-id">PDB ID</th>
<th class="reference">Reference</th>
</tr>
</thead>
<tbody>
{table_rows_html}</tbody>
</table>
</div>
</div>

<style>
/* Container for the entire table section */
.table-container {{
  max-width: 100%;
  margin: 0 auto;
  font-family: Arial, sans-serif;
}}

/* Table header text */
.table-header {{
  text-align: center;
  margin-bottom: 10px;
  font-size: 14px;
  color: #666;
}}

/* Responsive container */
.table-responsive {{
  overflow-x: auto; /* Allows horizontal scrolling if table is too wide */
  margin-bottom: 20px;
  border-radius: 4px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}}

/* Base table styling */
.puzzle-table {{
  width: 100%;
  border-collapse: collapse;
  /* Remove table-layout: fixed to allow auto layout */
  background-color: #fff;
  font-size: 14px;
}}

/* Table header styling */
.puzzle-table thead th {{
  background-color: #f0f0f0;
  color: #333;
  font-weight: bold;
  padding: 12px 10px; /* Increased padding */
  text-align: left;
  border: 1px solid #ddd;
  white-space: normal; /* Allow headers to wrap */
  vertical-align: bottom;
}}

/* Add hover effect to headers */
.puzzle-table th:hover {{
  background-color: #e0e0e0;
  cursor: pointer;
}}

/* Table cell styling */
.puzzle-table td {{
  padding: 8px 10px; /* Adjusted padding */
  border: 1px solid #ddd;
  vertical-align: top; /* Align content to the top */
  white-space: normal; /* Allow all cells to wrap */
  word-wrap: break-word; /* Break long words if necessary */
}}

/* Alternating row colors */
.puzzle-table tbody tr:nth-child(odd) {{
  background-color: #f9f9f9;
}}

.puzzle-table tbody tr:hover {{
  background-color: #f0f8ff;
}}

/* Column-specific styling */
/* Set min-widths to ensure readability */
.puzzle-id {{
  min-width: 100px;
  font-weight: bold;
  white-space: nowrap; /* Keep Puzzle ID on one line */
}}

.submission-date {{
  min-width: 130px;
  white-space: nowrap; /* Keep date on one line */
}}

.pdb-id {{
  min-width: 80px;
  white-space: nowrap; /* Keep PDB ID on one line */
}}

/* Reference column styling for wrapping */
.reference {{
  /* No specific width, let it take remaining space */
  hyphens: auto;
}}

/* Link styling */
.puzzle-table a {{
  color: #0066cc;
  text-decoration: none;
  /* Removed link-specific overflow/ellipsis */
}}

.puzzle-table a:hover {{
  text-decoration: underline;
  color: #004080;
}}

/* Responsive adjustments */
@media (max-width: 768px) {{
  .puzzle-table {{
    font-size: 13px;
  }}

  .puzzle-table th, .puzzle-table td {{
    padding: 6px 5px; /* Adjusted padding */
  }}

  .puzzle-id {{ min-width: 80px; }}
  .submission-date {{ min-width: 110px; }}
  .pdb-id {{ min-width: 60px; }}

  .table-header {{
    font-size: 12px;
  }}
}}
</style>

"""
    return html_content

# --- Main Script ---
if __name__ == "__main__":
    markdown_data = []
    if not POSTS_DIR.is_dir():
        print(f"Error: Directory not found - {POSTS_DIR}")
    else:
        print(f"Scanning directory: {POSTS_DIR}")
        for filename in os.listdir(POSTS_DIR):
            if filename.endswith(".markdown") or filename.endswith(".md"):
                filepath = POSTS_DIR / filename
                # print(f"Processing Markdown: {filename}") # Reduced verbosity
                data = extract_data_from_file(filepath)
                if data:
                    markdown_data.append(data)
        print(f"Extracted data for {len(markdown_data)} puzzles from Markdown.")

    # Extract data from Excel file
    excel_data = extract_data_from_excel(EXCEL_FILE)
    print(f"Extracted data for {len(excel_data)} puzzles from Excel.")

    # Combine the data
    all_data = markdown_data + excel_data
    print(f"\nTotal puzzles to display: {len(all_data)}")

    # Generate HTML
    html_output = generate_html_table(all_data)

    # Ensure the output directory exists
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    # Write HTML to file
    try:
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            f.write(html_output)
        print(f"\nSuccessfully generated HTML table at: {OUTPUT_FILE}")
    except Exception as e:
        print(f"\nError writing output file {OUTPUT_FILE}: {e}")