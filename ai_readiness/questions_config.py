QUESTIONS = [

    # ================================================================
    # 1. BUSINESS FIT (3 questions)
    # ================================================================

    {
        "id": "BF1",
        "section": "Business Fit",
        "label": "How clearly defined are your AI-related business goals?",
        "type": "rating",
        "dimension": "business_fit",
        "weight": 1.5,
        "scale_descriptions": {
            1: "No defined AI goals or unclear expectations.",
            2: "Some ideas exist but not well-formulated.",
            3: "Clear goals for certain areas, but not organization-wide.",
            4: "Well-defined goals aligned to business priorities.",
            5: "Highly structured AI vision with measurable outcomes."
        }
    },

    {
        "id": "BF2",
        "section": "Business Fit",
        "label": "How well do current business processes support AI implementation?",
        "type": "rating",
        "dimension": "business_fit",
        "weight": 1.0,
        "scale_descriptions": {
            1: "Processes are manual and inconsistent.",
            2: "Somewhat structured but lacking clarity.",
            3: "Moderately standardized processes across teams.",
            4: "Processes are well-documented and consistent.",
            5: "Highly optimized processes designed for automation and AI."
        }
    },

    {
        "id": "BF3",
        "section": "Business Fit",
        "label": "Which functional areas are most aligned with potential AI value?",
        "type": "multi_choice",
        "options": ["Customer Service", "Operations", "Sales & Marketing", "Finance", "IT Services"],
        "dimension": "business_fit",
        "weight": 1.0,
        "multi_choice_help": "Select all areas where AI can deliver measurable business impact."
    },


    # ================================================================
    # 2. LEADERSHIP (3 questions)
    # ================================================================

    {
        "id": "LD1",
        "section": "Leadership Readiness",
        "label": "How aligned is leadership with AI-driven initiatives?",
        "type": "rating",
        "dimension": "leadership",
        "weight": 1.5,
        "scale_descriptions": {
            1: "No leadership support.",
            2: "Minimal interest with limited involvement.",
            3: "Leadership is aware and moderately supportive.",
            4: "Strong support with active involvement.",
            5: "Leadership is fully committed and driving AI initiatives."
        }
    },

    {
        "id": "LD2",
        "section": "Leadership Readiness",
        "label": "How confident is leadership in investing in AI programs?",
        "type": "rating",
        "dimension": "leadership",
        "weight": 1.0,
        "scale_descriptions": {
            1: "No willingness to invest in AI.",
            2: "Limited budget consideration.",
            3: "Conditional investment based on ROI.",
            4: "Confident investment mindset with planning underway.",
            5: "High conviction with dedicated AI budget."
        }
    },

    {
        "id": "LD3",
        "section": "Leadership Readiness",
        "label": "How urgent is AI adoption from a strategic perspective?",
        "type": "single_choice",
        "options": ["Immediate", "High Priority", "Medium Priority", "Low Priority"],
        "dimension": "leadership",
        "weight": 1.0,
        "option_tooltips": {
            "Immediate": "AI adoption is mission-critical and urgent.",
            "High Priority": "Leadership wants to begin within a short timeframe.",
            "Medium Priority": "AI adoption is important but not urgent.",
            "Low Priority": "AI adoption is exploratory with no immediate plans."
        }
    },


    # ================================================================
    # 3. WORKFORCE (3 questions)
    # ================================================================

    {
        "id": "WF1",
        "section": "Workforce Preparedness",
        "label": "How equipped is your workforce to adopt AI solutions?",
        "type": "rating",
        "dimension": "workforce",
        "weight": 1.5,
        "scale_descriptions": {
            1: "No AI awareness or skills.",
            2: "Basic awareness but limited capability.",
            3: "Moderate AI literacy across some teams.",
            4: "Teams have practical AI experience.",
            5: "Workforce is highly skilled in AI technologies."
        }
    },

    {
        "id": "WF2",
        "section": "Workforce Preparedness",
        "label": "How adaptable is your workforce to process or technology changes?",
        "type": "rating",
        "dimension": "workforce",
        "weight": 1.0,
        "scale_descriptions": {
            1: "Very resistant to change.",
            2: "Occasionally adopts new workflows.",
            3: "Moderately adaptable with training.",
            4: "Highly adaptable to new tools and processes.",
            5: "Change-ready culture with continuous learning."
        }
    },

    {
        "id": "WF3",
        "section": "Workforce Preparedness",
        "label": "What internal AI competencies exist within your teams?",
        "type": "single_choice",
        "options": ["Strong team", "Basic knowledge", "Exploring", "None"],
        "dimension": "workforce",
        "weight": 1.0,
        "option_tooltips": {
            "Strong team": "You have internal AI engineers and analysts.",
            "Basic knowledge": "Some employees understand AI concepts.",
            "Exploring": "Teams are still learning or experimenting.",
            "None": "No AI skill or knowledge currently available."
        }
    },


    # ================================================================
    # 4. DATA MATURITY (3 questions)
    # ================================================================

    {
        "id": "DT1",
        "section": "Data Maturity",
        "label": "How structured and organized is your organizational data?",
        "type": "rating",
        "dimension": "data",
        "weight": 1.5,
        "scale_descriptions": {
            1: "Unstructured, fragmented, inconsistent data.",
            2: "Basic organization with significant gaps.",
            3: "Moderately structured with some governance.",
            4: "Well-structured with good governance.",
            5: "Highly structured, governed, accessible datasets."
        }
    },

    {
        "id": "DT2",
        "section": "Data Maturity",
        "label": "How reliable is your data in terms of accuracy and consistency?",
        "type": "rating",
        "dimension": "data",
        "weight": 1.0,
        "scale_descriptions": {
            1: "Data is highly unreliable and inconsistent.",
            2: "Some accuracy issues remain.",
            3: "Moderately reliable data with occasional errors.",
            4: "Generally reliable and monitored.",
            5: "Fully trusted, accurate, high-quality data."
        }
    },

    {
        "id": "DT3",
        "section": "Data Maturity",
        "label": "Where does most of your organizational data reside?",
        "type": "single_choice",
        "options": ["On-prem", "Hybrid", "Cloud"],
        "dimension": "data",
        "weight": 1.0,
        "option_tooltips": {
            "On-prem": "Data stored primarily on local servers.",
            "Hybrid": "Mix of cloud and on-prem storage.",
            "Cloud": "Data stored primarily in cloud platforms."
        }
    },


    # ================================================================
    # 5. ADOPTION READINESS (3 questions)
    # ================================================================

    {
        "id": "AD1",
        "section": "Adoption Readiness",
        "label": "How ready is your organization to integrate AI tools into daily workflows?",
        "type": "rating",
        "dimension": "adoption",
        "weight": 1.5,
        "scale_descriptions": {
            1: "Not ready at all.",
            2: "Limited readiness with major blockers.",
            3: "Moderate readiness with some dependencies.",
            4: "Good readiness with minor blockers.",
            5: "Fully ready with supporting infrastructure."
        }
    },

    {
        "id": "AD2",
        "section": "Adoption Readiness",
        "label": "How mature is your current automation landscape?",
        "type": "rating",
        "dimension": "adoption",
        "weight": 1.0,
        "scale_descriptions": {
            1: "Highly manual operations.",
            2: "Some automation exists but very limited.",
            3: "Moderate level of automation.",
            4: "Well-established automation frameworks.",
            5: "Automation-driven culture with optimized workflows."
        }
    },

    {
        "id": "AD3",
        "section": "Adoption Readiness",
        "label": "Have you adopted any cloud AI or ML services yet?",
        "type": "single_choice",
        "options": ["Yes", "No", "Experimenting"],
        "dimension": "adoption",
        "weight": 1.0,
        "option_tooltips": {
            "Yes": "AI/ML services are in active use.",
            "No": "No cloud AI tools have been adopted.",
            "Experimenting": "Your teams are evaluating or trialing AI tools."
        }
    }

]
