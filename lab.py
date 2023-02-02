import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

# basic page configuration
st.set_page_config(page_title='Luitel Lab', page_icon=":microscope:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#Use Local CSS

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")


# LOAD_ASSETS

afu_image = Image.open("images/AFU.jpg")
microscope = "https://cdn.pixabay.com/photo/2014/04/03/11/08/microscope-311859__340.png"
lottie1 = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_nkc7twjj.json")
lottie2 = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_wghjmogb.json")
lab_member_1 = Image.open("images/sample_image1.jpg")
lab_member_2 = Image.open("images/sample_image2.jpg")


# --- HEADER SECTION ---
col1, col2 = st.columns((2,1))
with col2:
    st.image(microscope, width=230)

with col1:
    st.title("Luitel Lab")
    st.markdown("### A team of Biotechnologist from Nepal")
    st.write("Centre for Biotechnology, Agriculture and Forestry University")
    st.write("📫", "hluitel@afu.edu.np")


# CONTENTS
homepage_intro_1 = """
Welcome to Luitel Lab, a cutting-edge biotechnology research facility located in Nepal.
The laboratory was established in 2010 and since then, we have been working towards improving animal and plant health through biotechnology.
Our lab is dedicated to advancing the field of biotechnology and improving human life through innovative scientific research.
"""
homepage_intro_2 = """
With a team of highly skilled and dedicated scientists, we are at the forefront of discovery in a wide range 
of biotechnology areas, from developing new vaccines and treatments for diseases, to creating sustainable agricultural 
solutions and improving food security.
Our main research areas of interest include Molecular Diagnostics, Animal Forensics, Reproductive Biotechnology, 
and Animal Genomics.
Under Molecular Diagnostics, we are working on the detection, isolation, and characterization of pathogens in both 
plants and animals to develop rapid diagnostic tools. We are also focused on characterizing livestock breeds and their 
relationship with traits of economic importance. Our state-of-the-art facility is equipped with the latest technologies and tools, 
allowing us to conduct cutting-edge research and achieve breakthrough results.
"""
homepage_intro_3 = """
Our focus is on collaboration, 
both within our lab and with other researchers and organizations around the world.
We believe that science has the power to change the world, and we are committed to making a positive impact 
through our work. Whether you are a fellow researcher, a student interested in biotechnology, or simply 
curious about what we do, we invite you to explore :mag_right: our website and learn more about Luitel Lab.
"""

with st.container():
    font_css = """
    <style>
    button[data-baseweb="tab"] > div[data-testid="stMarkdownContainer"] > p {
      font-size: 24px;
    }
    </style>
    """

    st.write(font_css, unsafe_allow_html=True)

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([":star: Home    ", ":mag: Research    ", ":mortar_board: Publications",
                                                  ":family: Our Team", ":camera: Media", ":telephone_receiver: Contact Us!!"])

    with tab1:
       # st.header("Home")
       with st.container():
           st.title("Hi ! Welcome to Luitel Lab :pray: ")
           # st.write("[Learn More >](https://www.google.com/)")
           st.write(homepage_intro_1)
           with st.container():
               left_column, right_column = st.columns((2,1))
               with left_column:
                   st.write(homepage_intro_2)
               with right_column:
                   st_lottie(lottie2, height=200, key="coding1")
           st.write(homepage_intro_3)
           st.markdown("#### We are passionate about integrating biology with technological advancement to develop innovative solutions of real world problems !!")


    with tab2:
       # What we do:
       with st.container():
           st.write("---")
           left_column, right_column = st.columns(2)
           with left_column:
               st.header("What We do")
               st.write(
                   """
               We are currently working on:
               - Developing rapid molecular diagnostic techniques of common pathogenic bacteria of poultry (E. Coli, Salmonella, Clostridium perfringens and Mycoplasma)
               - Molecular Diagnostic of Avian Pathogenic E. coli (APEC) in Commercial Poultry Birds in Chitwan District, Nepal
               - Wildlife genetics and Molecular study of infectious diseases of wildlife
               """)
           with right_column:
               st_lottie(lottie1, height=300, key="coding")

       # Research Interests

       with st.container():
           st.write("---")
           st.header("Research Interests:")
           st.markdown(
               "- Molecular Pathomechanism of pulmonary hypertension in experimental animals, High altitude medicine")
           st.markdown(
               "- Poultry disease: Molecular characterization of major poultry pathogens from Nepalese flocks, developing rapid diagnostic tools")
           st.markdown("- Vaccinology")
           st.markdown("- Nano technology in livestock and poultry disease diagnosis")
           st.markdown("- Wild life genetics and genetic study of infectious disease of wildlife")

    with tab3:
       st.markdown("### Have a look at our work on [Google Scholar]('https://scholar.google.com/citations?user=PJcQIW0AAAAJ&hl=en')")
       # st.write("CONTENTS OF this TAB")

    with tab4:
       with st.container():
           st.write("---")
           st.header("Lab Members")
           st.write("##")
           image_column, text_column = st.columns((1, 2))
           with image_column:
               st.image(lab_member_1)
           with text_column:
               st.subheader("Mr. ABC")
               st.write("""
               ABC is a researcher at XYZ lab since 2019. He focus on biotechnology and developing innovative medicines.
               His expertise and dedication have resulted in numerous breakthroughs in the field, positioning him as a leader in the industry.
               """)
               st.markdown("[Know more about him](https://www.google.com/)")
           image_column, text_column = st.columns((1, 2))
           with image_column:
               st.image(lab_member_2)
           with text_column:
               st.subheader("Ms. DEF")
               st.write("""
                    DEF is a researcher at our lab since 2019. She focus on biotechnology and developing innovative medicines.
                    Her expertise and dedication have resulted in numerous breakthroughs in the field, positioning her as a leader in the industry.
                    """)
               st.markdown("[Know more about her](https://www.google.com/)")



    with tab5:
        st.header("Pictures")
        st.write("here we will be posting cool pictures of our lab! ")

    with tab6:
        # Contact
        with st.container():
            st.write("---")
            st.header("Get In Touch With Us:")
            st.write("##")

            contact_form = """
            <form action="https://formsubmit.co/poudelmohit88@gmail.com" method="POST">
                <input type="hidden" name="_captcha" value="false">
                <input type="text" name="name" placeholder = "Your name" required>
                <input type="email" name="email" placeholder = "Your email" required>
                <textarea name="message" placeholder= "Your message here" required></textarea>
                <button type="submit">Send</button>
            </form>
            """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()




















