from app.modules.jobs.service import calculate_job_stats

def test_calculate_job_stats():
    # 1. SETUP: Create a controlled sample of data
    mock_data = {
        "count": 3,
        "results": [
            {
                "title": "Python Backend Engineer",
                "company": {"display_name": "TechFlow"},
                "location": {"display_name": "Remote"},
                "description": "This is a fully remote position."
            },
            {
                "title": "Data Scientist",
                "company": {"display_name": "Health Analytics"},
                "location": {"display_name": "Austin, TX"},
                "description": "On-site role in Texas."
            },
            {
                "title": "Junior Python Developer",
                "company": {"display_name": "TechFlow"},
                "location": {"display_name": "Remote"},
                "description": "Work from anywhere."
            }
        ]
    }

    # 2. EXECUTE: Pass the fake data into your function
    result = calculate_job_stats(mock_data)

    # 3. ASSERT: Verify the function returns the exact numbers it should
    assert result["Total_jobs"] == 3
    assert result["Remote_jobs"] == 2
    
    # TechFlow shows up twice, Health Analytics shows up once
    assert result["top_companies"] == ["TechFlow", "Health Analytics"]