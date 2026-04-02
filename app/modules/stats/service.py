from collections import Counter

def calculate_job_stats(adzuna_data):
    # Extract the list of jobs from the JSON dictionary
    jobs_list = adzuna_data.get("results", [])

    # 1. Calculate Total Jobs
    total_jobs = len(jobs_list)

    # 2. Calculate Remote Jobs
    remote_jobs = 0
    for job in jobs_list:
        location_name = job.get("location", {}).get("display_name", "").lower()
        description = job.get("description", "").lower()
        
        # Check if the job mentions remote work
        if "remote" in location_name or "remote" in description:
            remote_jobs += 1

    # 3. Calculate Top Companies
    company_names = []
    for job in jobs_list:
        # Grab the company name, default to "Unknown" if it's missing
        name = job.get("company", {}).get("display_name", "Unknown")
        company_names.append(name)
    
    # Use Counter to find the most frequently occurring companies
    company_tally = Counter(company_names)
    # Grab the top 3 most common companies
    top_companies = [company[0] for company in company_tally.most_common(3)]

    # Return the final formatted statistics
    return {
        "Total_jobs": total_jobs,
        "Remote_jobs": remote_jobs,
        "top_companies": top_companies
    }