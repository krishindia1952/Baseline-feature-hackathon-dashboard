import streamlit as st

# Page setup
st.set_page_config(page_title="Baseline Safe Web Features", layout="wide")
st.title("🛡️ Baseline-Safe Web Features Dashboard")
st.markdown("""
This dashboard highlights **HTML tags**, **CSS properties**, and **JavaScript APIs** that are considered safe to use across all major browsers.  
Each item includes examples and practical use cases to help developers build reliable web experiences.
""")

# HTML Tags
html_tags = [
    {"name": "<p>", "example": "<p>This is a paragraph.</p>", "use_cases": ["Text content", "Readable layout", "Semantic structure"]},
    {"name": "<div>", "example": "<div class='container'></div>", "use_cases": ["Layout container", "Grouping elements", "Styling hooks"]},
    {"name": "<span>", "example": "<span style='color:red'>Red text</span>", "use_cases": ["Inline styling", "Text emphasis", "Tooltips"]},
    {"name": "<a>", "example": "<a href='https://example.com'>Visit</a>", "use_cases": ["Navigation", "External links", "Download triggers"]},
    {"name": "<img>", "example": "<img src='logo.png' alt='Logo'>", "use_cases": ["Display images", "Icons", "Visual branding"]},
    {"name": "<form>", "example": "<form><input type='text'></form>", "use_cases": ["User input", "Data collection", "Authentication"]},
    {"name": "<button>", "example": "<button>Click Me</button>", "use_cases": ["Trigger actions", "Submit forms", "Interactive UI"]}
]

# CSS Properties
css_props = [
    {"name": "color", "example": "color: blue;", "use_cases": ["Text styling", "Theme design", "Accessibility"]},
    {"name": "margin", "example": "margin: 10px;", "use_cases": ["Spacing", "Layout control", "Visual balance"]},
    {"name": "display", "example": "display: flex;", "use_cases": ["Flexbox layout", "Responsive design", "Element arrangement"]},
    {"name": "font-size", "example": "font-size: 16px;", "use_cases": ["Readability", "Typography", "Responsive scaling"]},
    {"name": "border-radius", "example": "border-radius: 8px;", "use_cases": ["Rounded corners", "Modern UI", "Card design"]},
    {"name": "transition", "example": "transition: all 0.3s;", "use_cases": ["Smooth animations", "Hover effects", "State changes"]}
]

# JavaScript APIs
js_apis = [
    {"name": "document.querySelector()", "example": "document.querySelector('#main')", "use_cases": ["DOM selection", "Element manipulation", "Dynamic updates"]},
    {"name": "addEventListener()", "example": "button.addEventListener('click', handler)", "use_cases": ["Event handling", "User interaction", "Custom behaviors"]},
    {"name": "setTimeout()", "example": "setTimeout(() => alert('Hi'), 1000)", "use_cases": ["Delay actions", "Animations", "Polling"]},
    {"name": "fetch()", "example": "fetch('/api/data')", "use_cases": ["Data fetching", "API calls", "Dynamic content"]},
    {"name": "localStorage", "example": "localStorage.setItem('theme', 'dark')", "use_cases": ["Save preferences", "Offline support", "Session persistence"]},
    {"name": "JSON.parse()", "example": "JSON.parse('{\"name\":\"John\"}')", "use_cases": ["Data conversion", "API response handling", "Storage decoding"]}
]

# Tabs
tabs = st.tabs(["HTML Tags", "CSS Properties", "JavaScript APIs"])

with tabs[0]:
    st.header("✅ Always-Safe HTML Tags")
    for tag in html_tags:
        with st.expander(tag["name"]):
            st.markdown(f"**Example:** `{tag['example']}`")
            st.markdown("**Use Cases:**")
            for use in tag["use_cases"]:
                st.markdown(f"- {use}")

with tabs[1]:
    st.header("🎨 Always-Safe CSS Properties")
    for prop in css_props:
        with st.expander(prop["name"]):
            st.markdown(f"**Example:** `{prop['example']}`")
            st.markdown("**Use Cases:**")
            for use in prop["use_cases"]:
                st.markdown(f"- {use}")

with tabs[2]:
    st.header("📦 Always-Safe JavaScript APIs")
    for api in js_apis:
        with st.expander(api["name"]):
            st.markdown(f"**Example:** `{api['example']}`")
            st.markdown("**Use Cases:**")
            for use in api["use_cases"]:
                st.markdown(f"- {use}")
