from app.modules.stats.service import calculate_job_stats

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
    assert result["top_companies"] == ["TechFlow", "Health Analytics"]


def test_calculate_job_stats_empty_response():
    # 1. SETUP: Simulate Adzuna finding zero jobs
    mock_empty_data = {
        "count": 0,
        "results": []
    }

    # 2. EXECUTE: Pass the empty data into your function
    result = calculate_job_stats(mock_empty_data)

    # 3. ASSERT: Verify the math gracefully handles the zeros
    assert result["Total_jobs"] == 0
    assert result["Remote_jobs"] == 0
    assert result["top_companies"] == []