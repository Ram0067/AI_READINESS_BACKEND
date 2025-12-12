from .scoring import get_category

CATEGORY_DETAILS = {
    "AI Aspirant": (
        "AI Aspirant: The Foundation Phase\n"
        "You are in the early stages of AI adoption. Your organization is still establishing the core "
        "elements needed for successful AI deployment—data readiness, workflow clarity, and leadership alignment.\n\n"
        "**We Understand:** At this stage, you need a partner who can simplify complexity, educate stakeholders, "
        "and help you identify where AI can realistically deliver value.\n\n"
        "**Forgebyte’s Partnership Approach:** We guide you in building strong digital and data foundations, ensuring "
        "your teams understand AI capabilities and limitations. Our structured discovery workshops help you identify "
        "high-impact, low-risk areas to begin your AI journey.\n\n"
        "Ready to unlock your organization’s AI potential? Connect with us at Assist@forgebyte.com."
    ),

    "AI Explorer": (
        "AI Explorer: The Experimentation Phase\n"
        "Your organization is exploring AI possibilities and beginning to pilot early use cases. "
        "You have growing awareness and some foundational readiness, but scaling AI remains a challenge.\n\n"
        "**We Understand:** You need clarity on what works, what doesn’t, and how to prioritize use cases "
        "that truly move the needle.\n\n"
        "**Forgebyte’s Partnership Approach:** We help validate your early initiatives, refine your strategy, and "
        "design scalable AI frameworks. With industry examples—like predictive demand planning in Retail or "
        "automated claim triage in Insurance—we help you accelerate from testing to delivering measurable value.\n\n"
        "Looking to turn AI experiments into real ROI? Our experts are here to help."
    ),

    "AI Adopter": (
        "AI Adopter: The Transformation Phase\n"
        "You possess mature technical infrastructure, and AI is integrated into core business units. "
        "You are ready to leverage advanced capabilities—such as Generative AI—to unlock competitive advantage. "
        "Your focus now is on optimization, responsible governance, and realizing organization-wide transformation.\n\n"
        "**We Understand:** At this level, you need a partner who can challenge your existing systems and drive true "
        "differentiation. You require expertise not just in deployment but in governance, compliance, and continuous AI refinement.\n\n"
        "**Forgebyte’s Partnership Approach:** We go beyond implementation and serve as your long-term innovation lab. "
        "Using deep cross-industry expertise—such as hyper-personalized customer experiences in Retail or accelerated "
        "drug discovery workflows in Healthcare—we bring next-generation AI to your enterprise.\n\n"
        "We help optimize cost-to-serve, reinforce ethical AI practices, and ensure your models evolve responsibly.\n\n"
        "Ready to future-proof your leadership position with transformative AI?\n"
        "Engage our innovation team at Assist@forgebyte.com for a strategy session.\n\n"
        "**Our Commitment:** Sustainable, innovation-driven AI growth."
    ),

    "AI Transformer": (
        "AI Transformer: The Leadership Phase\n"
        "Your organization is operating at the forefront of AI maturity. AI is a strategic asset embedded deeply "
        "into products, workflows, and decision-making. You are pioneering innovation and setting the benchmark for your industry.\n\n"
        "**We Understand:** You need a partner capable of co-innovating cutting-edge systems—autonomous agents, ethical "
        "AI governance frameworks, real-time AI-driven decision engines, and next-gen personalization.\n\n"
        "**Forgebyte’s Partnership Approach:** We collaborate with your executive and engineering teams as an R&D "
        "accelerator, pushing boundaries across multimodal AI, experimentation infrastructure, and fully autonomous intelligent systems. "
        "Our vision is to ensure you maintain your competitive edge for the next decade.\n\n"
        "Let’s redefine what’s possible. Reach out for executive collaboration at Assist@forgebyte.com."
    ),
}


def generate_feedback(dim_scores, overall_score):
    category = get_category(overall_score)

    # Sort to identify strongest & weakest dimension
    sorted_dims = sorted(dim_scores.items(), key=lambda x: x[1], reverse=True)
    best_dim, best_val = sorted_dims[0]
    weak_dim, weak_val = sorted_dims[-1]

    return {
        "category": category,
        "summary": (
            f"Your AI Readiness Score is **{overall_score}%**, placing you in the "
            f"**{category}** category. Your strongest capability is **{best_dim.replace('_',' ').title()} ({best_val})**, "
            f"while **{weak_dim.replace('_',' ').title()} ({weak_val})** represents the area of greatest opportunity."
        ),
        "profile": (
            f"Your organization shows strong performance in **{best_dim.replace('_',' ').title()}**, indicating maturity "
            f"in that area. However, improving **{weak_dim.replace('_',' ').title()}** will accelerate your AI execution."
        ),
        "category_detail": CATEGORY_DETAILS[category],
        "recommended_actions": [
            "Identify 2–3 high-ROI AI use cases tailored to your maturity level.",
            "Enhance data literacy and AI skill development across teams.",
            "Establish or strengthen AI governance and responsible-AI practices.",
            "Initiate or scale pilot programs with measurable success metrics.",
            "Drive cross-functional alignment for AI-led transformation.",
        ]
    }
