from collections import Counter

def calculate_job_stats(jobs_data: dict) -> dict:
    """
    Calculates statistics from the live Adzuna jobs data.
    """
    # 1. Extract the actual list of jobs from Jerri's dictionary
    jobs_list = jobs_data.get("jobs", [])

    # Handle the empty edge case gracefully
    if not jobs_list:
        return {
            "total_jobs": 0,
            "remote_jobs": 0,
            "top_companies": [],
            "top_locations": []
        }

    total_jobs = len(jobs_list)
    remote_jobs = 0
    companies = []
    locations = []

    # 2. Loop through the live data to do our math
    for job in jobs_list:
        title = (job.get("title") or "").lower()
        location = (job.get("location") or "").lower()
        
        # We use 'Unknown' as a fallback if Adzuna is missing data
        company_name = job.get("company") or "Unknown"
        location_name = job.get("location") or "Unknown"

        # Check if the job is remote based on title or location
        if "remote" in title or "remote" in location:
            remote_jobs += 1

        companies.append(company_name)
        locations.append(location_name)

    # 3. Use Python's Counter to find the 3 most common companies and locations
    top_companies = [comp for comp, count in Counter(companies).most_common(3)]
    top_locations = [loc for loc, count in Counter(locations).most_common(3)]

    # Return the clean, lowercase dictionary
    return {
        "total_jobs": total_jobs,
        "remote_jobs": remote_jobs,
        "top_companies": top_companies,
        "top_locations": top_locations
    }