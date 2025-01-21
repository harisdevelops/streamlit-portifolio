import streamlit as st

# Set page configuration
st.set_page_config(page_title="Haris Masood Portfolio", layout="wide")

# Sidebar content
st.sidebar.image("pic.jpeg", width=250)  


st.sidebar.image("image.png", width=250)

# Main content with tabs
tabs = st.tabs(["Home", "About Me", "Projects", "Skills", "Contact"])

with tabs[0]:
    # Home Section
    st.title("Hello! Dev Haris here")
    st.write("### Web Application Developer & Data Scientist")
    st.write("**My Workings**")
    st.write("""
    - **Deep Learning Models for Predictive Analytics**: Designed and implemented deep learning models to derive insights and improve decision-making processes.
    - **Statistical Analysis and Modeling**: Applied advanced statistical methods such as hypothesis testing and regression analysis for data-driven insights.
    - **Frontend Development**: Skilled in building responsive and interactive user interfaces for web applications using React.js.
    - **Cloud Computing**: Implemented scalable cloud services using Google Cloud Platform (GCP) to enhance application performance and reliability.
    - **Backend Development**: Designed and developed robust server-side solutions using Node.js.
    """)

    st.write("### Connect with Me")
    st.markdown(
        """
        <div style="text-align: center;">
            <p>Connect me on:</p>
            <a href="https://www.linkedin.com/in/haris-masood-b53370246/" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="LinkedIn" width="30" style="margin: 0 5px;">
            </a>
            <a href="https://github.com/harisdevelops" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" alt="GitHub" width="30" style="margin: 0 5px;">
            </a>
            
        </div>
        """,
        unsafe_allow_html=True
    )

with tabs[1]:
  
    st.title("About Me")

    st.markdown("<h3 class='section-subtitle'>Education</h3>", unsafe_allow_html=True)
    st.markdown("""
    - *Bachelor's in Data Science* • University of Central Punjab, Lahore (2022 – Present)                                                  Grade: 3.85
    """)

    st.markdown("<h3 class='section-subtitle'>Experience</h3>", unsafe_allow_html=True)
    st.markdown("""
    - *React Developer* • Freelancing • Lahore (May 2022 – Present)   
    - *Data Scientist* • Prodigy Tech (October 2024 – Present)  
    - *MERN Stack Lab Instructor* • PNY  • Lahore (Dec 2022 – Present)   
    - *FULL Stack Developer* • NEXUS Berry (May 2021 – Nov 2022)     
    """)

with tabs[2]:
    # Projects Section
    st.title("Projects")
    
    # Row 1: Project 1 and Project 2
    col1, col2 = st.columns(2)
    with col1:
        st.write("### Pak Express Luxury Car Transport")
        st.image("pe.png", width=500)  # Replace with your image path
        st.write(""" 
        - Description: A Cab Booking Web App for a company Based In Dubai.
        - Technologies: Full-Stack Development, Nex.js, GCP
        - [Link](https://www.pakexpresslimousine.com/)
        """)
    with col2:
        st.write("### ATL WorldWide Limousine")
        st.image("al.png", width=500)  # Replace with your image path
        st.write(""" 
        - Description: A scalable and user-friendly limousine booking app for a company based in Atlanta, USA.
        - Technologies: React.js, Node.js, MongoDB
        - [Link](https://atlworldwidelimousine.com/)
        """)
    
    # Row 2: Project 3 
    col3, _ = st.columns([2, 1])  # Adjust column width ratios as needed
    with col3:
        st.write("### Project 3: Mars Spaceship Landing Prediction")
        st.write(""" 
        - Description: A deep learning model, which predicts the success rate of spaceship landing on Mars.
        - Technologies: Python, TensorFlow, Keras, PyTorch
        - [GitHub Link](https://github.com/harisdevelops/IBMcourse1st.git)
        """)


with tabs[3]:
    # Skills Section
    def skills_section():
        st.markdown('<h2 class="section-title">Skills</h2>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.write("*Programming*")
            st.progress(0.95)
            st.write("Solved over 100+ leetcoding question, which are asked in big tech interviews .")

            st.write("*Web application development*")
            st.progress(0.95)
            st.write("3 years+ experience in web application development using diff trending frameworks and libraries.")
        with col2:
            st.write("*Deep Learning*")
            st.progress(0.8)
            st.write("Skilled in using deep learning algorithms .")
            
            st.write("*Data analysis*")
            st.progress(0.75)
            st.write("Skilled in  Statistical analysis and visulisation of data.")

    # Call the skills_section function to render the updated content
    skills_section()


    



    st.write("""
    - *Programming Languages:* Python, JavaScript, C++
    - *Web Development:* React.js, Node.js, nextjs, XML, JSON HTML/CSS, bootstrap, Material UI, Ant UI, GCP
    - *Data Science & Machine Learning:* TensorFlow, Pandas, NumPy, Knime, Pentaho
    - *Tools & Platforms:* Git, Docker, Google Cloud, Github
    """)

with tabs[4]:
    # Contact Section
    st.title("Contact Me")
    st.write("""
    Feel free to reach out to me via the following channels:

    - *Email:* your-email@example.com
    - *Phone:* +123-456-7890
    - *GitHub:* [Your GitHub](https://github.com/your-github-profile)
    - *LinkedIn:* [Your LinkedIn](https://www.linkedin.com/in/haris-masood-b53370246/)
    """)

    st.write("### Contact Form")
    with st.form(key="contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit = st.form_submit_button("Send")

        if submit:
            st.success("Thank you for your message! I will get back to you soon.")