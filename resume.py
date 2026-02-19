def save_resume(resume_data, filename="resumes.json"):
    """Save resume data to JSON file"""
    try:
        # Step 1: Try to load existing data
        try:
            with open(filename, 'r') as f:
                resumes = json.load(f)  # Load existing resumes
        except FileNotFoundError:
            resumes = []  # File doesn't exist yet
        
        # Step 2: Add new resume
        resumes.append(resume_data)
        
        # Step 3: Save back to file
        with open(filename, 'w') as f:
            json.dump(resumes, f, indent=2)  # Write with formatting
        
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False