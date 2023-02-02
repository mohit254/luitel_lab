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
lottie_contact_us = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_lt8ter7g.json")
# lottie_contact_us = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_px0ntw70.json")
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

publications_list = """
- Subedi M, Bhattarai RK, Devkota B, Phuyal S & Luitel H, Antibiotic resistance pattern and virulence genes content in avian pathogenic Escherichia coli (APEC) from broiler chickens in Chitwan, Nepal, [BMC Vet Res.](https://www.ncbi.nlm.nih.gov/pubmed/29789009#) 2018 May 22;14(1):166. doi: 10.1186/s12917-018-1453-9.
- Luitel H, Sydykov A, Schermuly RT, Pressure overload leads to an increased accumulation and activity of mast cells in the right ventricle, Physiological Reports, DOI: 10.14814/phy2.13146
- Pradhan, K., Sydykov, A., Tian, X., Mamazhakypov, A., Neupane, B., Luitel, H., . . . Kretschmer, A. (2016). Soluble guanylate cyclase stimulator riociguat and phosphodiesterase 5 inhibitor sildenafil ameliorate pulmonary hypertension due to left heart disease in mice. International journal of cardiology, 216, 85-91.
- Luitel H, Sydykov, A, Seimetz M et al, Pulmonary Vascular Research in Nepal: Prospective and Challenges, PVRI Chronicle: Volume 2 Issue 1 January - June 2015.
- Kosanovic, D., Luitel, H., Dahal, B. K., Cornitescu, T., Janssen, W., Danser, A. J., . . . Schiffers, P. (2015). Chymase: a multifunctional player in pulmonary hypertension associated with lung fibrosis. European Respiratory Journal, ERJ-00182-02015.
- Petrovic, A., Seimetz, M., Sydykov, A., Pak, O., Veit, F., Luitel, H., . . . Schermuly, D. K. Cold-induced pulmonary hypertension: a distinctive pathological entity of the pul-monary circulation?, Volume 2 Issue 1 January - June 2015.
- Janssen, W., Schymura, Y., Novoyatleva, T., Kojonazarov, B., Boehm, M., Wietelmann, A, Luitel H., . . . Tretyn, A. (2015). 5-HT2B receptor antagonists inhibit fibrosis and protect from RV heart failure. BioMed research international, 2015.
- Kojonazarov B, Luitel H, Sydykov A, Dahal BK, Ghofrani HA, Schermuly RT, PPAR delta activation ameliorates right ventricular function in pressure overload induced RVH model.  Pulm Circ. 2014 Jun;4(2):352.
- Kojonazarov, B., Novoyatleva, T., Sabiska, Z., Janssen, W., Tian, X., Luitel, H., . . . Grimminger, F. (2014). Inhibition of P38 Mapk Improves Heart Function in Sustained Pressure-overload Induced Right Ventricular Hypertrophy and Failure. Circulation, 130(Suppl 2), A15100-A15100.
- Luitel, H. (2013). Mast Cells in Pressure Overload Induced Right Ventricular Remodeling, American Thoracic Society.
- Kojonazarov, B., Sydykov, A., Pullamsetti, S. S., Luitel, H., Dahal, B. K., Kosanovic, D., . . . Evans, S. (2013a). Effects of multikinase inhibitors on pressure overload-induced right ventricular remodeling. International journal of cardiology, 167(6), 2630-2637.
- Kojonazarov, B., Luitel, H., Sydykov, A., Dahal, B. K., Paul-Clark, M. J., Bonvini, S. J., . . . Mitchell, J. A. (2013b). The Effects PPAR / Agonist GW0742 On Right Heart Hypertrophy And Function, American Thoracic Society.
- Kojonazarov, B., Luitel, H., Sydykov, A., Dahal, B. K., Paul-Clark, M. J., Bonvini, S., . . . Mitchell, J. A. (2013a). The peroxisome proliferator–activated receptor β/δ agonist GW0742 has direct protective effects on right heart hypertrophy. Pulmonary circulation, 3(4), 926-935.
- Kosanovic D, Kojonazarov B, Luitel H, Schermuly RT et al, Therapeutic efficacy of TBC3711 in monocrotaline-induced pulmonary hypertension. Respir Res., 2011 June 23;12(1):87.
- Janssen, W., Schymura, Y., Wietelmann, A., Stasch, J.-P., Luitel, H., Weissmann, N., . . . Seeger, W. (2011b). Improvement of right heart structure and function by BAY 41-8543 in pulmonary artery banded mice. BMC Pharmacology, 11(S1), P79.
- Kosanovic, D., Kojonazarov, B., Luitel, H., Dahal, B. K., Sydykov, A., Cornitescu, T., . . . Ghofrani, H. A. (2011). Therapeutic efficacy of TBC3711 in monocrotaline-induced pulmonary hypertension. Respiratory research, 12(1), 87.
- Luitel, H., Sydykov, A., Kojonazarov, B., Dahal, B. K., Kosanovic, D., Seeger, W., . . . Schermuly, R. (2011). Contribution of progenitor cells in experimental right heart hypertrophy induced by pulmonary artery ligation. Pneumologie, 65(S 01), P175.
- Krompiec, D., Janssen, W., Pullamsetti, S. S., Schymura, Y., Luitel, H., Ghofrani, H., . . . Seeger, W. (2011). Terguride attenuates myocardial remodelling and diastolic dysfunction in the pressure overloaded right heart. Pneumologie, 65(S 01), P307.
- Schymura, Y., Janssen, W., Luitel, H., Stasch, J., Weißmann, N., Ghofrani, H.-A., . . . Schermuly, R. (2011). Effects of BAY 41–8543 in an Animal Model of Right HeartHypertrophy. Pneumologie, 65(S 02), S134-S134
- Janssen W, Schymura Y, Wietelmann A, Johannes-Peter Stasch, Luitel H, Schermuly RT et al, Improvement of right heart structure and function by BAY 41-8543 in pulmonary artery banded mice, BMC Pharmacology 01/2011; 11:1-2. DOI:10.1186/1471-2210-11-S1-P79
- Luitel Het al., Contribution of progenitor cells in experimental right heart hypertrophy induced by pulmonary artery ligation. American Thoracic Society (ATS), May 1, 2011, A4980-A4980.
- Kojonazarov, B., Kosanovic, D., Pullamsetti, S. S., Sydykov, A., Luitel, H., Tian, X., . . . Barnard, R. (2010). Reversal Of Experimental Pulmonary Hypertension By The Multi-kinase Inhibitor Sunitinib, American Thoracic Society.
- Amirjanians, V., Egemnazarov, B., Sydykov, A., Kojonazarov, B., Luitel, H., Weissmann, N., . . . Ghofrani, H. (2010). Inhalative application of soluble guanylyl cyclase stimulator BAY 41–8543 for treatement of pulmonary arterial hypertension. Pneumologie, 64(S 03), P419.
- Amirjanians, V, Egemnazarov, B., Sydykov, A., Kojonazarov, B., Luitel, H., Weissmann, N., . . . Ghofrani, H. (2010). Inhalative application of soluble guanylyl cyclase stimulator BAY 41–8543 for treatement of pulmonary arterial hypertension. Pneumologie, 64(S 03), P419.
- Luitel H, et al., Right ventricular remodeling in response to pressure overload, Pneumologie, 2010; 64 - P336, DOI: 10.1055/s-0030-1251352
- Luitel H, Milk fever in four different buffaloes, The Blue Cross, Vol 6, 2005.
- Luitel H, An effective brooding of chicks, The Blue Cross, Vol 6, 2003
"""

ongoing_research_activities = """

**a. Translational Research**

- Establishment and validation of laboratory animal experimental unit for pulmonary hypertension (In Collaboration with Justus-Liebig University, Giessen, Germany)

**b. Poultry diseases**

- Developing rapid molecular diagnostic techniques of common pathogenic bacteria of poultry (E. Coli, Salmonella, Clostridium perfringens and Mycoplasma)
- Molecular Diagnostic of Avian Pathogenic E. coli (APEC) in Commercial Poultry Birds in Chitwan District, Nepal
    
**c. Wildlife genetics and Molecular study of infectious diseases of wildlife**
- Molecular sexing of captive vultures from vulture breeding center, Kasara, Chitwan National Park, Nepal (In collaboration with NTNC and BCN)-Completed

- Prevalence of Elephant endotheliotropic Herpes Virus type 1 in Asymptomatic Asian Elephants of Chitwan District, Nepal

- Genetic diversity of Red Panda from Nepal Himalaya (In collaboration with Himali Conservation Forum and funded by USAID/WWF/Hariyo Ban Program)

- Genetic diversity of Swamp Deer population from Shuklaphanta and Bardia National Park. (In collaboration with NTNC and funded by USAID/WWF/Hariyo Ban Program)

- Triad study of (Ecological, Infections and Genetic) of Gharial in Gharial Breeding Center (GBC) (In collaboration with CNP and funded by USAID/WWF/Hariyo Ban Program)

- Genetic diversity of Musk Deer population from Nepal Himalaya (In collaboration with NTNC and funded by USAID/WWF/Hariyo Ban Program)
"""

what_you_can_expect_from_me = """
Our aim is to cultivate an environment that nurtures your growth and development as a researcher. 
As your advisor, I am dedicated to supporting you on your academic journey and helping you achieve your goals. 
**Here's what you can expect from me:**

### Development as an Independent Researcher
My primary focus is to guide you in developing your skills as an independent researcher. 
This includes training in the literature, concepts, methods, and research process in your field, as well as professional
skills such as writing, presenting, goal-setting, and time-management.

### Availability
I am available for regular one-on-one meetings and provide feedback on your work. 
I have weekly check-ins with students who are leading research projects and bi-weekly check-ins with students who have 
other priorities for the term. I maintain an open-door policy for quick questions, 
and will provide honest and constructive feedback on your research progress.

### Transparency and Communication
To ensure that you receive the best possible guidance, I request that you provide at least two weeks' notice for 
feedback on your work, and that you inform me in advance of any important deadlines. 
I will also inform you in advance of any anticipated periods of travel or leave, and arrange alternative support 
during my absence.

### Supportive Environment
I am committed to creating a lab environment that is safe, respectful, and supportive, where you can freely 
discuss your ideas and produce valid research. I will also assist you in transitioning to the next stage of your 
career, whether academic or non-academic, and point you towards networking opportunities 
such as conferences and workshops.

### Recommendation Letters
When it comes to writing recommendation letters, I will be honest and transparent in my assessment. 
To ensure that I am able to provide you with the best possible letter, please give me at least two weeks' 
notice and provide me with all relevant information, such as: the opportunity for which you are applying; 
the due date; the name, institution and address of the person/committee to whom the letter should be addressed; 
instructions on how to submit the letter (email address, physical address, etc) and; any instructions on what the 
letter should discuss. Send a reminder 3-5 days before the deadline.
"""

contact_us = """
At the Luitel Lab, we believe in creating a welcoming and inclusive environment for students of all backgrounds 
to pursue their academic goals. 
Our team is dedicated to supporting and mentoring students in the development of their research projects, 
which are closely aligned with our own research initiatives in the fields biotechnology.

**As an advisor, my goal is to help you become a confident, knowledgeable, and independent researcher. Throughout the process, I will work with you to:**

- Produce high-quality work

- Expand your understanding of ecology and evolution

- Develop research projects that align with your interests and career goals

- Identify knowledge gaps, current relevant questions, and feasible methods for investigation

This journey is both challenging and rewarding, and requires a strong commitment from both you and me. 
I am dedicated to providing regular one-on-one meetings and support to help you succeed. 
You will also have the opportunity to participate in lab meetings, seminars, 
and engage with other research groups on campus.

***At the Luitel Lab, we believe in fostering a welcoming, safe, respectful, and supportive environment for all persons. We value the diverse perspectives and backgrounds of our team members and strive to create an inclusive atmosphere for everyone***.
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
           st.markdown("- Molecular Pathomechanism of pulmonary hypertension in experimental animals, High altitude medicine")
           st.markdown("- Poultry disease: Molecular characterization of major poultry pathogens from Nepalese flocks, developing rapid diagnostic tools")
           st.markdown("- Vaccinology")
           st.markdown("- Nano technology in livestock and poultry disease diagnosis")
           st.markdown("- Wild life genetics and genetic study of infectious disease of wildlife")
           st.write("---")
           st.header("Ongoing Research Activities:")
           st.markdown(ongoing_research_activities)

    with tab3:
       st.markdown("### Have a look at our work on [Google Scholar]('https://scholar.google.com/citations?user=PJcQIW0AAAAJ&hl=en')")
       st.markdown("#### Here is the list of my published articles:")
       st.markdown(publications_list)


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
            st.markdown(contact_us)
            st.write("---")
            st.markdown(what_you_can_expect_from_me)
            st.write("---")
            st.header("Get In Touch With Us:")
            # st.write("##")

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
        with right_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with left_column:
            st_lottie(lottie_contact_us, height=300, key="coding3")
