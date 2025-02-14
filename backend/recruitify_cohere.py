from dotenv import load_dotenv
import pdfplumber
import os
from langchain_cohere.chat_models import ChatCohere
from langchain_cohere.react_multi_hop.agent import create_cohere_react_agent
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
cohere_api_key = os.getenv("COHERE_API")

def pdf_to_text(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def generate_script():
    resume = pdf_to_text("./uploads/resume.pdf")
    job_description = """
    About the job
    About 1Password

    We all have important information we need to manage, and protecting it should be easy. Over 150,000 businesses and millions of people log in to 1Password to unlock smart, simple access to everything they care about. Our vision is to create a safer, simpler digital future for everyone, and our culture values simplicity, honesty and a human-centric approach to solving problems. Come help us unlock peace of mind so everyone can stay safer online.

    Software powers the world, and we empower those who write it. We are on a mission to make worldwide developers’ daily lives easier and more secure. We do that by building tools that eliminate accepted complexity, turning historically complex, confusing, and frustrating tasks into delightful automated processes. This makes developers more productive and protects businesses throughout the entire software development lifecycle: from writing and committing code to testing in CI, deploying, and finally running in production.

    Teams hiring interns: Developer Growth - building features that help external developers streamline their daily workflows.


    Remote by design.  1Password has been remote-first since our inception in 2005, meaning that we’re no stranger to building digital community and culture. With our teams fully remote and located all around the world, we stay connected through company-wide events, coffee chats, fun Slack channels, and peer-to-peer recognition through Bonusly — just to name a few. Our remote environment means that you have the flexibility to make those midday workout classes, take your dog out for a walk when they need one, and run errands on your own schedule. As an intern, you can expect to set core hours with your manager, and then work when you’re at your best. We all thrive in different conditions, so we encourage you to make your workday work for you! 💙

    This is a remote opportunity within Canada. This is a full time (40 hours per week) position that will run for 4 months - May to August 2025.

    What You Can Expect

    Build tools that help developers and developer admins simplify and streamline their daily workflows using 1Password.
    Challenge the status quo, and help make the secure way of doing development, the easy way. Remove accepted complexity from developers' lives.
    Integrate with third party developer tools, like GitHub Actions, Kubernetes, CircleCI, and a whole lot more.
    Collaborate with people from across many countries, disciplines and experience levels, who all care a lot about what we’re building.


    What We're Looking For

    Confidence: A willingness to take on new challenges, and see them through to completion.
    Humility: You're not afraid to ask "stupid" questions and make mistakes (as long as you learn from them).
    Curiosity: You look for better ways of doing things, even if everyone seems happy with how they are.
    Teamwork: We work together, and succeed as a team!


    Bonus Points For

    Experience with Rust, Golang, Typescript, and/or React.
    Experience with or an interest in improving developers lives by writing scripts, tools, or finding other workflow optimizations.
    Experience with Git, SSH, Commit Signing, 1Password Command Line Tool, CI/CD pipelines and/or cloud providers.


    Even if you don't tick all those boxes, we'd like to hear from you. 

    The most important thing you can bring to this job is the drive to dive in, get the work done, and fix root causes instead of treating symptoms. We believe in continuous learning and support professional development on the job with a budget to back it up. If you bring a desire to do the right thing for our customers, a sense of ownership over the product you work on, and a focus on shipping quality code, we want to hear from you.

    This role will close on Friday, February 14th, 2025.

    What We Offer

    We believe in working hard, and resting hard. We’re always looking for new ways to support our team members, but here’s a glance at what we currently offer:

    > 🏝 Generous PTO policy - 2.08 days per month (1.5 work weeks per 4 month term)

    > 💖 Company-wide wellness days off scheduled throughout the year

    > 🌎 Employee-led DEIB programs and ERGs and ECGs

    > 🏠 Fully remote environment

    > 🏆 Peer-to-peer recognition through Bonusly

    > 💡 1Password University access and learning sessions

    > 🥳 Monthly internship events and socials

    You belong here. 

    1Password is proud to be an equal opportunity employer. We are committed to fostering an inclusive, diverse and equitable workplace that is built on trust, support and respect. We welcome all individuals and do not discriminate on the basis of gender identity and expression, race, ethnicity, disability, sexual orientation, colour, religion, creed, gender, national origin, age, marital status, pregnancy, sex, citizenship, education, languages spoken or veteran status. Be yourself, find your people and share the things you love. 

    Accommodation is available upon request at any point during our recruitment process. If you require an accommodation, please speak to your talent acquisition partner or email us at nextbit@agilebits.com and we’ll work to meet your needs. 

    Remote work is a part of our DNA. Given that our company was founded remotely in 2005, we can safely say we're experts at building remote culture. That said, remote work at 1Password does mean working from your home country. If you've got questions or concerns about this, your talent partner would be happy to address them with you.

    Successful applicants will be required to complete a background check that may consist of prior employment verification, reference checks, education confirmation, criminal background, publicly available social media, credit history, or other information, as permitted by local law.

    1Password uses an automated employment decision tool as a part of the recruitment process. See the latest bias audit information . A reasonable accommodation, reasonable alternative selection process, appeal or to exercise your right to opt-out of AADM may be requested by emailing  nextbit@agilebits.com with subject "AI accommodation request". For additional information see our Candidate Privacy Notice .
    """
    writing_sample = """
    Today I will talk about black body radiation.

    Before I explain what blackbody radiation is, you need to know what a blackbody is. An ideal blackbody is a surface that absorbs all electromagnetic radiation that strikes it, making it appear black. However, because nothing can absorb all wavelengths equally and perfectly, ideal blackbodies don’t exist, and real-world applications of blackbodies end up reflecting some electromagnetic radiation.

    This image of a box with a hole in it serves as a conceptual representation of a blackbody. The light that passes through the hole has a hard time getting back out. If you were to look into the hole, it would be pitch black, indicating that most of the light that passes through the hole is absorbed by the body itself. 

    In our universe, the closest things to an ideal blackbody that we know of so far are celestial bodies like the Sun.

    What is blackbody radiation? Blackbody radiation is the thermal electromagnetic radiation emitted by a blackbody at thermodynamic equilibrium with its environment. Blackbodies emit radiation of the same wavelength as the vibrations of the molecules making up the black body.

    This slide shows the graphs of blackbody radiation emitted for 2 different objects. The y-axis is spectral power density, which means the intensity of that wavelength emitted, and the x-axis is the wavelength. The rainbow just represents the visible spectrum. On the left, we have a light bulb. As you can see, most of the graph is in the area with longer wavelengths and peaks in the infrared wavelength. However, it still reaches the visible spectrum, reaching a lot of the red and orange wavelengths and a bit of the other colors as well. Thus, as demonstrated by the RGB color model at the top of the graph, there is mostly red light with a bit of green light, and just a little bit of blue light; which ends up producing an orange light. On the right, we have the Sun. You can see, this graph is vastly different and is mostly in the visible spectrum. As a result, all colors are present, and we see white with a bit of green because it peaks in the green area. However, it is such a small difference that our eyes aren’t able to see the higher intensity of the green light. 

    """

    prompt = ChatPromptTemplate.from_template("""
    Based on the following resume and job description and writing_sample, create a compelling 2-paragraph pitch from the resume owner's point of view in the style and tone similar to the writing sample. Only return the pitch:
        
        WRITING SAMPLE:
        {writing_sample}

        RESUME:
        {resume}
        
        JOB DESCRIPTION:
        {job_description}
        
        Create a personalized pitch that:
        1. Shows enthusiasm for the company and role in the first paragraph
        2. Highlights relevant achievements and potential contributions in the second paragraph
        3. Ends with a polite request for an interview or coffee chat
        4. Maintains a professional yet engaging tone
        5. Is specific to the role and company
        """)

    llm = ChatCohere(
        model="command-r-plus", 
        temperature=0.5, 
        api_key=cohere_api_key)

    chain = prompt | llm

    response = chain.invoke({
        "writing_sample" : writing_sample,
        "resume": resume,
        "job_description": job_description
    })

    return response.content

def main():
    print(generate_script())


if __name__ == '__main__':
    main()