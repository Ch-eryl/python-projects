import random
from datetime import datetime, timedelta

class ProjectSimulator:
    def __init__(self):
        self.project_types = [
            "Web Application", "Data Analysis", "Machine Learning", 
            "Game Development", "Automation Script", "Computer Vision",
            "Natural Language Processing", "Blockchain", "IoT System",
            "API Development", "Desktop Application", "Mobile App"
        ]
        
        self.technologies = {
            "Web Application": ["Django", "Flask", "FastAPI", "React", "Vue.js"],
            "Data Analysis": ["Pandas", "NumPy", "Matplotlib", "Seaborn", "Plotly"],
            "Machine Learning": ["Scikit-learn", "TensorFlow", "PyTorch", "Keras"],
            "Game Development": ["Pygame", "Arcade", "Panda3D", "Godot"],
            "Automation Script": ["Selenium", "BeautifulSoup", "Requests", "Scrapy"],
            "Computer Vision": ["OpenCV", "Pillow", "SimpleCV"],
            "Natural Language Processing": ["NLTK", "spaCy", "Gensim", "Transformers"],
            "Blockchain": ["Web3.py", "Pyethereum", "Pycoin"],
            "IoT System": ["MicroPython", "CircuitPython", "RPi.GPIO"],
            "API Development": ["FastAPI", "Flask-RESTful", "Django REST"],
            "Desktop Application": ["PyQt", "Tkinter", "Kivy", "PyGTK"],
            "Mobile App": ["Kivy", "BeeWare", "PyQT"]
        }
        
        self.difficulties = ["Beginner", "Intermediate", "Advanced", "Expert"]
        self.challenges = [
            "Time constraints", "Complex requirements", "Learning new technology",
            "Performance optimization", "Debugging tricky issues", "Data quality problems",
            "Integration with external systems", "Security concerns", "Scalability challenges",
            "Cross-platform compatibility"
        ]
        
        self.team_roles = [
            "Developer", "Data Scientist", "UI/UX Designer", 
            "Project Manager", "QA Engineer", "DevOps"
        ]
        
    def generate_project(self):
        project_type = random.choice(self.project_types)
        tech_stack = random.sample(self.technologies[project_type], k=random.randint(2, 4))
        difficulty = random.choice(self.difficulties)
        
        # Estimate duration based on difficulty
        duration_weeks = {
            "Beginner": random.randint(1, 3),
            "Intermediate": random.randint(2, 6),
            "Advanced": random.randint(4, 10),
            "Expert": random.randint(8, 20)
        }[difficulty]
        
        start_date = datetime.now()
        end_date = start_date + timedelta(weeks=duration_weeks)
        
        # Random challenges
        num_challenges = random.randint(1, 3)
        project_challenges = random.sample(self.challenges, k=num_challenges)
        
        # Team composition
        team_size = random.randint(1, 5)
        team = random.sample(self.team_roles, k=team_size)
        
        return {
            "name": f"{project_type} Project",
            "type": project_type,
            "tech_stack": tech_stack,
            "difficulty": difficulty,
            "duration_weeks": duration_weeks,
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d"),
            "challenges": project_challenges,
            "team": team,
            "budget": f"${random.randint(1000, 50000)}",
            "description": f"Build a {project_type.lower()} using {', '.join(tech_stack)}."
        }
    
    def simulate_development(self, project):
        print(f"\nStarting project: {project['name']}")
        print(f"Description: {project['description']}")
        print(f"Team: {', '.join(project['team'])}")
        print(f"Tech Stack: {', '.join(project['tech_stack'])}")
        print(f"Difficulty: {project['difficulty']}")
        print(f"Estimated Duration: {project['duration_weeks']} weeks")
        print(f"Budget: {project['budget']}")
        print("\nDevelopment progress:")
        
        weeks_completed = 0
        success = True
        
        while weeks_completed < project['duration_weeks']:
            weeks_completed += 1
            progress = min(100, int((weeks_completed / project['duration_weeks']) * 100))
            
            # Random event
            event_chance = random.random()
            if event_chance > 0.7:  # 30% chance of an event
                event_type = random.choice(["challenge", "breakthrough", "requirement_change"])
                
                if event_type == "challenge":
                    challenge = random.choice(project['challenges'])
                    print(f"Week {weeks_completed}: Facing {challenge.lower()} - progress slowed")
                    if random.random() > 0.6:  # 40% chance of delay
                        delay = random.randint(1, 2)
                        project['duration_weeks'] += delay
                        print(f"  ! Project delayed by {delay} weeks !")
                elif event_type == "breakthrough":
                    print(f"Week {weeks_completed}: Major breakthrough! Progress accelerated")
                    if random.random() > 0.7:  # 30% chance of time saved
                        time_saved = random.randint(1, 2)
                        project['duration_weeks'] = max(1, project['duration_weeks'] - time_saved)
                        print(f"  ! Project shortened by {time_saved} weeks !")
                else:
                    print(f"Week {weeks_completed}: Requirements changed - some rework needed")
            else:
                print(f"Week {weeks_completed}: Steady progress - {progress}% complete")
            
            # Check for project failure (5% chance each week after week 2)
            if weeks_completed > 2 and random.random() > 0.95:
                print(f"\nWeek {weeks_completed}: Critical failure! Project cancelled.")
                success = False
                break
        
        if success:
            print(f"\nProject completed in {weeks_completed} weeks!")
            print("Final result: Successfully delivered project")
        else:
            print("Final result: Project failed")
        
        return success

def main():
    print("This is your Python Project Simulator")
    print("------------------------\n")
    
    simulator = ProjectSimulator()
    
    while True:
        print("\nOptions:")
        print("1. Generate new project")
        print("2. Simulate project development")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            project = simulator.generate_project()
            print("\nGenerated Project:")
            for key, value in project.items():
                print(f"{key.replace('_', ' ').title()}: {value}")
        elif choice == "2":
            try:
                project = simulator.generate_project()
                simulator.simulate_development(project)
            except Exception as e:
                print(f"Error during simulation: {e}")
        elif choice == "3":
            print("Exiting simulator...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
