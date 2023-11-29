import streamlit as st
import plotly.graph_objects as go
from random import sample

questions = [
    # Technical vs Non-Technical
    "I grasp how AI algorithms learn and make decisions.",
    "The intricacies of AI make its ethical deployment challenging.",
    "I would feel comfortable explaining how a neural network works to a friend.",
    "I stay updated on AI advancements and their societal discussions.",
    "AI ethics should primarily involve those deeply versed in the technology.",
    "My trust in AI is based on its reliability, not the complexity behind it.",

    # Optimism vs Pessimism
    "AI will be a net positive for job creation.",
    "In the next two decades, AI will substantially elevate our quality of life.",
    "The media tends to exaggerate the risks associated with AI.",
    "I would feel comfortable allowing an AI tutor to teach my child.",
    "I would ask ChatGPT for help if I was CEO of my company.",
    "I believe that there will be no more AI winters.",

    # Agency vs Fatalism
    "Humans have the capacity to steer AI development effectively.",
    "AI's evolution is beyond significant human influence.",
    "I believe that we will always be able to shape AI's trajectory.",
    "AI's influence on our daily decision-making is overstated.",
    "I'm confident that I can adjust my career amidst AI changes.",
    "Current laws will adequately regulate AI's societal effects.",
]

# Questions aimed at evaluating views on AI
questionsx = [
    
    # Technical vs Non-Technical
    "I understand the basic principles behind how AI algorithms learn and make decisions",
    "The technical complexity of AI a barrier to its ethical and safe development",
    "One should have a technical background to make informed decisions about AI usage?",
    "Understanding AI algorithms is essential for responsibly using AI-driven platforms.",
    "The ethical considerations of AI should be left to experts with a deep understanding of the technology.",
    "I regularly follow the latest developments and discussions in the field of AI.",
    "My trust in AI applications is not influenced by the technology’s complexity, but by its demonstrated reliability and accuracy."

    # Optimism vs Pessimism
    "AI will create more jobs than it destroys",
    "AI will significantly improve our quality of life in the next two decades",
    "The risks of AI overblown by the media and society",
    "I feel optimistic about the role of AI in advancing healthcare",
    "Concerns about AI leading to widespread job displacement are overestimated.",
    "AI will play a crucial role in managing environmental sustainability.",
    "I am optimistic that AI will be instrumental in personalizing education to individual needs.",
    "The potential negative consequences of AI are likely to outweigh its benefits.",

    # Agency vs Fatalism
    "I believe humans can fully control AI development and its impacts",
    "The evolution of AI an inevitable process that humans can only marginally influence",
    "Individuals can meaningfully alter the course of AI advancements through their actions",
    "AI's development ultimately lead to outcomes beyond human control.",
    "I am confident in my ability to adapt my career in response to AI advancements.",
    "Legislation will be effective in managing AI’s societal impacts.",
    "It is too late to reverse the changes brought about by AI in certain industries.",
    "I believe that AI development is progressing in a way that aligns with humanity’s best interests.",
    "The influence of AI on our daily choices is often exaggerated.",
]

random_q_order = sample(range(0, 18), 18)
responses = [3] * 18 # = [3 for _ in range(18)]

# calculate each of 3 axes
def calculate_characteristics():
    agency_vs_fatalism = sum(responses[:6])
    optimism_vs_pessimism = sum(responses[6:12])
    technical_vs_nontechnical = sum(responses[12:])
    return agency_vs_fatalism/15-1, optimism_vs_pessimism/15-1, technical_vs_nontechnical/15-1


def classify_ai_personality(agency_score, optimism_score, technical_score):
    # Helper function to classify score
    def classify(score):
        if score >= 4: return 'High'
        elif score >= 2: return 'Medium'
        else: return 'Low'

    # Classify each score
    agency = classify(agency_score)
    optimism = classify(optimism_score)
    technical = classify(technical_score)

    # Mapping to AI personality types with emojis
    personalities = {
        ('High', 'High', 'High'): 'The Optimistic Warrior 💪🚀',
        ('High', 'High', 'Medium'): 'The Visionary Leader 👓🌟',
        ('High', 'High', 'Low'): 'The Idealistic Pioneer 🌱🔮',
        ('High', 'Medium', 'High'): 'The Informed Realist 🧠💼',
        ('High', 'Medium', 'Medium'): 'The Balanced Innovator ⚖️🛠️',
        ('High', 'Medium', 'Low'): 'The Pragmatic Dreamer 🤔💤',
        ('High', 'Low', 'High'): 'The Skeptical Technologist 🤖😒',
        ('High', 'Low', 'Medium'): 'The Cautious Strategist 🛡️🗺️',
        ('High', 'Low', 'Low'): 'The Grounded Activist 🌍✊',
        ('Medium', 'High', 'High'): 'The Tech-Savvy Optimist 📱😊',
        ('Medium', 'High', 'Medium'): 'The Ethical Guardian 🦸‍♂️👁️',
        ('Medium', 'High', 'Low'): 'The Hopeful Humanist ❤️🙏',
        ('Medium', 'Medium', 'High'): 'The Pragmatic Observer 👀🧐',
        ('Medium', 'Medium', 'Medium'): 'The Reflective Mediator 🪞✨',
        ('Medium', 'Medium', 'Low'): 'The Considerate Thinker 🌼🤝',
        ('Medium', 'Low', 'High'): 'The Cautious Analyst 🕵️‍♂️📉',
        ('Medium', 'Low', 'Medium'): 'The Deliberate Questioner ❓📚',
        ('Medium', 'Low', 'Low'): 'The Traditionalist 🏛️📜',
        ('Low', 'High', 'High'): 'The Tech-Savvy Visionary 🚀👀',
        ('Low', 'High', 'Medium'): 'The Intuitive Believer 🔮💫',
        ('Low', 'High', 'Low'): 'The Rebel Optimist 😎🌈',
        ('Low', 'Medium', 'High'): 'The Skeptical Technophile 📡🙄',
        ('Low', 'Medium', 'Medium'): 'The Doubting Professional 🏢🤷‍♂️',
        ('Low', 'Medium', 'Low'): 'The Conservative Observer 👵🔍',
        ('Low', 'Low', 'High'): 'The Intuitive Skeptic 🔍🤨',
        ('Low', 'Low', 'Medium'): 'The Wary Critic 🐢📖',
        ('Low', 'Low', 'Low'): 'The Doubtful Bystander 🛌👻'
    }

    return personalities.get((agency, optimism, technical), 'Undefined Personality')

# Streamlit app
def main():
    
    st.set_page_config(
        page_title='Your AI Identity',  # Add your app title here
        layout='centered',  # Can be "centered" or "wide". "wide" is the default.

    )
    st.sidebar.markdown('Find the original article at [MMI Impact Update](https://www.melbournemicrofinance.com/impactupdate?fbclid=IwAR3Igs_GccNYKUucYPulmFl8OnI1I5oMEpwBkCYWjUEuFlcjn6jnGCf1448)')
    st.sidebar.write('##### Made by Justin Lee')

    st.title("Your AI Identity")
    st.write("##### `1` = Strongly Disagree, `3` = Neutral, `5` = Strongly Agree")

    with st.form(key='questions_form'):
        for i in random_q_order: 
            answer = st.slider(questions[i], 1, 5, 3)
            responses[i] = answer
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        char1, char2, char3 = calculate_characteristics()
        st.write(f'##### Your AI personality is: ')
        st.write(f'# `{classify_ai_personality(char1, char2, char3)}`')
        st.write(f'##### See where you lie on the spectrum:')

        # 3D Plotting using Plotly
        fig = go.Figure(data=[go.Scatter3d(
            x=[char1],
            y=[char2],
            z=[char3],
            mode='markers',
            marker=dict(size=10, color='red', symbol='diamond')
        )])

        # Update the layout
        # ... [previous code remains the same]

        # Update the layout
        fig.update_layout(
            width = 700,
            height = 800,
            scene=dict(
                xaxis=dict(
                    title='Agency vs Fatalism',
                    range=[-1, 1]  # Set the range for x-axis
                ),
                yaxis=dict(
                    title='Optimism vs Pessimism',
                    range=[-1, 1]  # Set the range for y-axis
                ),
                zaxis=dict(
                    title='Technical vs Non-Technical',
                    range=[-1, 1]  # Set the range for z-axis
                )
            ),
        )

        st.plotly_chart(fig)

if __name__ == "__main__":
    main()
