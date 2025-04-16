# Filename: generate_puzzle_table.py
import os
import re
from pathlib import Path
from collections import defaultdict

# --- Configuration ---
POSTS_DIR = Path("_posts/results")
OUTPUT_FILE = Path("_includes/puzzle_list_table.html")
# --- End Configuration ---

def extract_data_from_file(filepath):
    """
    Extracts Puzzle ID, Submission/Deadline, PDB ID, and Reference from a single Markdown file.
    """
    puzzle_id = None
    puzzle_num = None  # Just the numeric part
    submission_deadline = ""  # Default to empty string
    pdb_id = ""  # PDB ID
    reference = ""  # Reference information
    detail_url = ""  # URL to the results (previously detail) page
    assessment_url = "" # URL to the assessment page (extracted but not used for now)

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            in_front_matter = False
            file_content = f.read()
            lines = file_content.splitlines()

            # First pass: Front Matter for Title and Date (for URL)
            date_str = ""
            for i, line in enumerate(lines):
                line = line.strip()
                if i == 0 and line == '---':
                    in_front_matter = True
                    continue
                if in_front_matter:
                    if line == '---':
                        in_front_matter = False
                        break # Stop after front matter
                    if line.startswith('title:'):
                        # Extract the title content
                        title_content = line.split(':', 1)[-1].strip().strip('"')
                        # Use the full title as puzzle_id
                        puzzle_id = title_content
                        # Try to extract numeric part
                        num_match = re.search(r'\d+', title_content)
                        if num_match:
                            puzzle_num = num_match.group()
                    elif line.startswith('date:'):
                        # Extract date for URL construction
                        date_str = line.split(':', 1)[-1].strip()
                        # Try to parse date in format like "2017-11-18 20:42:00 +0000"
                        date_match = re.search(r'(\d{4})-(\d{2})-(\d{2})', date_str)
                        if date_match:
                            year, month, day = date_match.groups()
                            # Format for URL path: /results/YYYY/MM/DD/
                            detail_url = f"/results/{year}/{month}/{day}/"

            # Extract PDB ID - pattern like: **PDB id**: [8hb8](...)
            pdb_match = re.search(r'\*\*PDB id\*\*\s*:\s*\[(.*?)\]', file_content)
            if pdb_match:
                pdb_id = pdb_match.group(1).strip()
            
            # Extract Submission/Deadline - try multiple patterns
            # Pattern 1: **Puzzle Submission/Deadline:** 2014.06.28/07.15
            submission_match1 = re.search(r'\*\*Puzzle Submission/Deadline:\*\*\s*([\d\.\/]+)', file_content)
            # Pattern 2: **Puzzle Submission/Deadline:** text 2014.06.28/07.15 text
            submission_match2 = re.search(r'\*\*Puzzle Submission/Deadline:\*\*.*?([\d]{4}\.[\d]{2}\.[\d]{2}/[\d]{2}\.[\d]{2})', file_content)
            # Pattern 3: Submission/Deadline anywhere in document
            submission_match3 = re.search(r'Submission/Deadline.*?([\d]{4}\.[\d]{2}\.[\d]{2}/[\d]{2}\.[\d]{2})', file_content)
            
            # Try each pattern in sequence
            if submission_match1:
                submission_deadline = submission_match1.group(1).strip()
            elif submission_match2:
                submission_deadline = submission_match2.group(1).strip()
            elif submission_match3:
                submission_deadline = submission_match3.group(1).strip()
                
            # Print debug info for troubleshooting
            print(f"File: {filepath.name}")
            print(f"  Extracted date: '{submission_deadline}'")
            
            # Fallback: look for any date pattern in YYYY.MM.DD/MM.DD format in whole file
            if not submission_deadline:
                date_anywhere = re.findall(r'(\d{4}\.\d{2}\.\d{2}/\d{2}\.\d{2})', file_content)
                if date_anywhere:
                    submission_deadline = date_anywhere[0]
                    print(f"  Fallback date found: '{submission_deadline}'")
            
            # Extract Reference - Pattern: **Reference**:
            # We want to extract text such as "Nature Chemical Biology 13, 508–513 (2017) doi:10.1038/nchembio.2333."
            # and any link like [Nature Chemical Biology 13, 508–513 (2017) doi:10.1038/nchembio.2333.](https://www.nature.com/...)
            reference_match = re.search(r'\*\*Reference\*\*:?\s*(.*?)(?:\*\*|\n\n|\Z)', file_content, re.DOTALL)
            if reference_match:
                ref_text = reference_match.group(1).strip()
                # Try to find a URL in the reference text
                url_match = re.search(r'\[(.*?)\]\((.*?)\)', ref_text)
                if url_match:
                    # If found, use the text and URL to create a link
                    ref_text_clean = url_match.group(1).strip()
                    ref_url = url_match.group(2).strip()
                    # Use the full reference text with link
                    reference = f"<a href='{ref_url}' target='_blank'>{ref_text_clean}</a>"
                else:
                    # If no URL, just use the text
                    reference = ref_text

        # Ensure puzzle_id was found
        if puzzle_id is None:
            print(f"Warning: Could not extract Puzzle ID from title in {filepath.name}")
            # Fallback: try to get ID from filename
            match = re.search(r'PZ(\d+)', filepath.stem, re.IGNORECASE)
            if match:
                puzzle_id = f"Puzzle {match.group(1)}"
                puzzle_num = match.group(1)
            else:
                puzzle_id = filepath.stem # Use stem as fallback ID
                puzzle_num = ""

        # Extract numeric part for sorting
        num_match = re.search(r'\d+', puzzle_id)
        sort_key = int(num_match.group()) if num_match else 9999
        
        # Complete the detail URL with the filename
        # Assuming filename is like 2017-11-18-PZ10.markdown
        # Extract PZ part
        pz_match = re.search(r'PZ\d+', filepath.stem, re.IGNORECASE)
        if pz_match:
            # Ensure detail_url base exists
            if detail_url:
                detail_url += f"{pz_match.group()}.html"
            else:
                print(f"Warning: Could not determine date for detail URL of {filepath.name}")
                detail_url = "#" # Fallback URL if date extraction failed
        else:
            # Fallback to original filename without date part and extension
            name_part = filepath.stem
            if '-' in name_part:
                # Remove date prefix like "2017-11-18-"
                name_part = name_part.split('-', 3)[-1] if len(name_part.split('-')) > 3 else name_part
            # Ensure detail_url base exists
            if detail_url:
                detail_url += f"{name_part}.html"
            else:
                print(f"Warning: Could not determine date for detail URL of {filepath.name}")
                detail_url = "#" # Fallback URL if date extraction failed
        
        # Construct the assessment URL (extracted but not used)
        if puzzle_num:
            assessment_url = f"/table/2000/01/01/PZ{puzzle_num}-3d.html"
        else:
            # If puzzle_num couldn't be extracted, try from filename
            if pz_match:
                assessment_url = f"/table/2000/01/01/{pz_match.group()}-3d.html"
            else:
                # Leave blank if cannot determine
                assessment_url = ""

        return {
            "id": puzzle_id,
            "dates": submission_deadline,
            "pdb_id": pdb_id,
            "reference": reference,
            "sort_key": sort_key,
            "detail_url": detail_url,
            "assessment_url": assessment_url # Still extracted, just not used in HTML
        }

    except Exception as e:
        print(f"Error processing file {filepath}: {e}")
        return None

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
        if item['pdb_id']:
            pdb_link = f"<a href='https://www.rcsb.org/structure/{item['pdb_id']}' target='_blank'>{item['pdb_id']}</a>"
        
        # Wrap puzzle ID in a link to the detail/results page
        puzzle_id_link = f"<a href='{item['detail_url']}'>{item['id']}</a>"
        
        # Reference content (can contain HTML links)
        reference_content = item['reference']

        table_rows_html += f"""<tr>
<td class="puzzle-id">{puzzle_id_link}</td>
<td class="submission-date">{item['dates']}</td>
<td class="pdb-id">{pdb_link}</td>
<td class="reference">{reference_content}</td> 
</tr>
""" # Removed title attribute, as content will wrap

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
<th class="submission-date">Submission/Deadline</th>
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
    all_data = []
    if not POSTS_DIR.is_dir():
        print(f"Error: Directory not found - {POSTS_DIR}")
        exit()

    print(f"Scanning directory: {POSTS_DIR}")
    for filename in os.listdir(POSTS_DIR):
        if filename.endswith(".markdown") or filename.endswith(".md"):
            filepath = POSTS_DIR / filename
            print(f"Processing: {filename}")
            data = extract_data_from_file(filepath)
            if data:
                all_data.append(data)

    print(f"\nExtracted data for {len(all_data)} puzzles.")

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