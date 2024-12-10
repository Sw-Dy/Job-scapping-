def fetch_jobs(role, location, experience):
    base_url = f"https://www.naukri.com/{role}-jobs-in-{location}-{experience}-years"
    print(f"Fetching jobs from: {base_url}")

    options = Options()
    options.headless = True
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    jobs = []  

    try:
        driver.get(base_url)
        
        # Extend the wait time
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.listContainer'))  # Adjust selector if necessary
        )

        # Increase sleep time for dynamic loading
        time.sleep(10)

        soup = BeautifulSoup(driver.page_source, 'lxml')

        job_listings = soup.find_all('div', class_='jobTuple')  # Adjust with correct class name

        if not job_listings:
            print("No job listings found.")
            return jobs

        for job_card in job_listings:
            try:
                job_title = job_card.find('a', class_='title').text.strip()  # Update with the correct class
                company_name = job_card.find('a', class_='subTitle').text.strip()  # Update with the correct class
                job_location = job_card.find('li', class_='location').text.strip()  # Update with the correct class
                job_experience = job_card.find('li', class_='experience').text.strip()  # Update with the correct class
                job_url = job_card.find('a', class_='title')['href']  # Update with the correct class
                
                jobs.append({
                    'Job Title': job_title,
                    'Company': company_name,
                    'Location': job_location,
                    'Experience': job_experience,
                    'URL': job_url
                })
            except AttributeError as e:
                print(f"Error parsing a job listing, skipping... Error: {e}")

    except Exception as e:
        print(f"An error occurred while fetching jobs: {e}")
    finally:
        driver.quit()

    if jobs:
        print(f"Total jobs found: {len(jobs)}")
    else:
        print("No jobs were found or there was an error in scraping.")
        
    return jobs
