import csv

# Define the path to the CSV file
csv_file_path = "/home/vignesh/Downloads/archive/survey.csv"

# Function to read and process the CSV file
def process_survey_data(file_path):
    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            
            # Skip the header row
            next(reader)
            
            # Initialize variables to store survey results
            total_participants = 0
            aware_of_issue = 0
            not_aware_of_issue = 0
            
            # Iterate through the survey data
            for row in reader:
                total_participants += 1
                awareness = row[3]  # Assuming awareness information is in column 4 (adjust as needed)
                
                if awareness.lower() == "yes":
                    aware_of_issue += 1
                else:
                    not_aware_of_issue += 1
            
            # Calculate awareness percentage
            awareness_percentage = (aware_of_issue / total_participants) * 100
            
            # Display awareness statistics
            print("Public Awareness Program Statistics:")
            print(f"Total Participants: {total_participants}")
            print(f"Aware of the Issue: {aware_of_issue}")
            print(f"Not Aware of the Issue: {not_aware_of_issue}")
            print(f"Awareness Percentage: {awareness_percentage:.2f}%")
            
            # Provide recommendations based on awareness
            if awareness_percentage < 50:
                print("Recommendation: There's a low awareness level. Consider awareness campaigns.")
            else:
                print("Recommendation: Good awareness! Continue efforts to maintain and increase awareness.")
    
    except FileNotFoundError:
        print("File not found:", file_path)
    except Exception as e:
        print("An error occurred:", str(e))

# Call the function to process the survey data and provide awareness statistics
process_survey_data(csv_file_path)
