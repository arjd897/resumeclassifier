import streamlit as st
import pickle
import pandas as pd

# Load the trained model
with open('scorepred.pkl', 'rb') as file:
    rf = pickle.load(file)

# Define the list of skills
all_skills = [
    "C", "C++", "Java", "Python", "JavaScript", "Data Structures and Algorithms",
    "Linux", "Windows", "UNIX", "SQL", "NoSQL", "MySQL", "MongoDB", "TCP/IP", 
    "Network Security", "Firewalls", "Version Control (Git)", "Agile", "DevOps", 
    "Ethical Hacking", "Cryptography", "Machine Learning", "Deep Learning", "NLP",
    "AWS", "Azure", "Google Cloud", "Android", "iOS", "Flutter", "R", "Pandas",
    "NumPy", "Data Cleaning", "Matplotlib", "Seaborn", "Tableau", "Power BI",
    "Scikit-learn", "TensorFlow", "Keras", "PyTorch", "Hadoop", "Spark", "Hive",
    "Text Mining", "Sentiment Analysis", "ETL Pipelines", "Data Warehousing",
    "Neural Networks", "CNNs", "RNNs", "Google BigQuery", "HTML", "CSS",
    "React.js", "Angular.js", "Vue.js", "Node.js", "Express.js", "Django",
    "Flask", "Ruby on Rails", "PostgreSQL", "GitHub", "Bootstrap", "Materialize",
    "Apache", "Nginx", "Heroku", "RESTful APIs", "GraphQL", "WordPress", "Joomla",
    "OWASP", "SSL/TLS", "CI/CD", "Docker", "OOPs", "Collections", "Multithreading",
    "Exception Handling", "Spring", "Spring Boot", "Hibernate", "Struts", 
    "Servlets", "JSP", "Web Services", "Maven", "Gradle", "SVN", "JUnit", "TestNG",
    "Mockito", "JDBC", "JPA", "Spring Cloud", "Netflix OSS", "Singleton", 
    "Factory", "Observer", "Java Security APIs", "SSL", "OAuth", "Data Types",
    "Control Structures", "Functions", "Modules", "Django", "Flask", "FastAPI",
    "Automation with Python", "Web Scraping", "BeautifulSoup", "Scrapy", "SQLite",
    "SQLAlchemy", "REST", "SOAP", "Encryption Libraries", "Docker", "Kubernetes",
    "Vagrant", "Terraform", "AWS CloudFormation", "Ansible", "GitLab CI", 
    "AWS S3", "Azure Blob", "Google Cloud Storage", "VPC", "Subnets", 
    "Load Balancing", "IAM", "Key Management Service", "Cloud Security Best Practices",
    "Serverless Computing", "AWS Lambda", "Azure Functions", "Google Cloud Functions",
    "AWS CloudWatch", "Prometheus", "Grafana", "AWS RDS", "DynamoDB", "Azure SQL Database",
    "STAAD Pro", "ETABS", "SAP2000", "Revit", "SketchUp", "Navisworks", "Primavera",
    "Microsoft Project", "Plaxis", "GeoStudio", "Total Station", "GPS", "GIS", 
    "EIA", "Water Treatment Process", "MX Roads", "Civil 3D", "Synchro", "BOQ Preparation",
    "Cost Estimation", "Contract Management", "HEC-RAS", "WaterGEMS", "StormCAD",
    "SolidWorks", "CATIA", "PTC Creo", "ANSYS", "Abaqus", "HyperMesh", "GD&T",
    "Tolerance Stack-up", "DFMEA", "HVAC Design", "Heat Transfer Simulation", 
    "CNC Machining", "Additive Manufacturing", "3D Printing", "Computational Fluid Dynamics",
    "Material Selection", "Failure Analysis", "Composite Materials", "PLC Programming",
    "SCADA", "Industrial Robotics", "Reliability Centered Maintenance", "RCM",
    "Predictive Maintenance", "Technical Writing", "Time Management and Organization",
    "Research and Development", "PowerPoint", "Prezi", "Project Management",
    "Risk Management"
]

st.title("Resume Score Predictor")

# User input for experience, skills, and company type
experience = st.number_input("Enter years of experience(including internship)", min_value=0, max_value=30, step=1)
selected_skills = st.multiselect("Select your skills(minimum 4 skills required)", all_skills)
other_skills = st.text_input("Enter other skills, if any")
company_type = st.selectbox("Select type of company(highest level you have worked in)", options=["Startup", "Mid-size", "Enterprise"])

# Calculate the number of selected skills
num_skills = len(selected_skills) + (1 if other_skills else 0)

# Map the company type to its numerical value
company_type_mapping = {'Startup': 0, 'Mid-size': 1, 'Enterprise': 2}
company_type_value = company_type_mapping[company_type]

# Create a DataFrame for the input data
input_data = pd.DataFrame([[experience, num_skills, company_type_value]], 
                          columns=['Experience in Years', 'Number of Skills', 'Type of Company'])
# Display the predicted total marks
if st.button("Predict"):
    y_pred_new = rf.predict(input_data)
    st.write(f"Predicted Resume Score is: {(y_pred_new[0]/12)*100:.2f}")
