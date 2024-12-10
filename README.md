# Job Scraper - README

## Overview

**Job Scraper** is a web scraping application designed to aggregate job postings from various platforms, including TimesJobs, FreshersWorld, AasaanJobs, Internshala, MyAMCAT, and JobGuru. The tool parses job listings, organizes them into JSON format, and provides a unified view of opportunities. This project is ideal for job seekers, career counselors, and recruiters who want to analyze job trends or find targeted job listings efficiently.

---

## Features

1. **Multi-Platform Scraping**  
   Supports job scraping from multiple platforms such as TimesJobs, AasaanJobs, FreshersWorld, and more.

2. **JSON Outputs**  
   Consolidates scraped data into JSON files for easy integration and analysis.

3. **Error Logging**  
   Maintains an `error.log` file to track issues encountered during scraping.

4. **Web Interface**  
   Provides an interface (`index.html`) for viewing and managing scraped data.

5. **Extensible**  
   Modular scripts (e.g., `timesjobs.py`, `myamcat.py`) allow for easy addition of new job platforms.

---

## File Structure

| File/Folder Name          | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| **LICENSE**               | Specifies the GPL-3.0 license for the repository.                         |
| **README.md**             | The detailed documentation of the project.                                |
| **aasaanjobs.json**       | Contains scraped job listings from AasaanJobs.                            |
| **app.py**                | Flask-based application to display and manage scraped data.               |
| **csv-json.py**           | Converts CSV data to JSON format.                                         |
| **error.log**             | Logs errors encountered during scraping.                                  |
| **freshersworld.json**    | Contains scraped job listings from FreshersWorld.                        |
| **headers.json**          | Stores HTTP headers used during web scraping.                             |
| **index.html**            | Web interface to view and interact with job listings.                    |
| **internshala.json**      | Contains scraped job listings from Internshala.                          |
| **jobguru.json**          | Contains scraped job listings from JobGuru.                              |
| **mentor.html**           | Provides mentorship-related content or resources.                         |
| **myamcat.json**          | Contains scraped job listings from MyAMCAT.                              |
| **myamcat.py**            | Script for scraping job listings from MyAMCAT.                           |
| **requirements.txt**      | Lists all dependencies required for the project.                         |
| **scraper.cpython-312.pyc** | Compiled Python bytecode for the scraper module.                        |
| **scraper.py**            | Core logic for scraping jobs across platforms.                           |
| **timesjobs.json**        | Contains scraped job listings from TimesJobs.                            |
| **timesjobs.py**          | Script for scraping job listings from TimesJobs.                         |

---

## Requirements

### Prerequisites
- Python 3.8 or higher
- Libraries (listed in `requirements.txt`):
  - Flask
  - requests
  - beautifulsoup4
  - pandas

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/job-scraper.git
   cd job-scraper
   ```
2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Running the Application
1. Start the Flask application:
   ```bash
   python app.py
   ```
2. Open the web interface in your browser at `http://127.0.0.1:5000`.

### Scraping Jobs
1. Run individual platform scripts (e.g., `timesjobs.py`, `myamcat.py`) to scrape data:
   ```bash
   python timesjobs.py
   python myamcat.py
   ```
2. The scraped data will be stored in corresponding JSON files (e.g., `timesjobs.json`).

### Viewing Results
- Access `index.html` to view the aggregated job listings in a structured format.

---

## Extending the Tool

### Adding New Platforms
1. Create a new script (e.g., `newplatform.py`) based on the structure of existing scripts.
2. Implement scraping logic using libraries like `requests` and `BeautifulSoup`.
3. Save the output in a new JSON file (e.g., `newplatform.json`).
4. Update the web interface or `app.py` if required.

---

## License

This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details.

---

## Contributions

Contributions are welcome! Fork the repository and submit a pull request for enhancements, bug fixes, or new scraping platforms.

---
