import streamlit as st

st.set_page_config(
    page_title="Student Grade AI",
    page_icon="🚀",
    layout="wide"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#020617,#0f172a,#111827);
    color:white;
}

/* Title */
.title{
    text-align:center;
    font-size:55px;
    font-weight:bold;
    color:#00e5ff;
    text-shadow:0 0 10px #00e5ff,
                0 0 20px #00e5ff;
    animation: glow 2s infinite alternate;
}

@keyframes glow{
    from{
        text-shadow:0 0 10px #00e5ff;
    }
    to{
        text-shadow:0 0 25px #00e5ff,
                    0 0 50px #00e5ff;
    }
}

/* Subtitle */
.subtitle{
    text-align:center;
    color:#94a3b8;
    margin-bottom:30px;
}

/* Cards */
.card{
    background:rgba(255,255,255,0.05);
    border:1px solid rgba(0,229,255,0.3);
    border-radius:20px;
    padding:25px;
    text-align:center;
    backdrop-filter:blur(15px);

    transition:0.4s;

    box-shadow:0 0 15px rgba(0,229,255,0.2);
}

.card:hover{
    transform:translateY(-8px);
    box-shadow:0 0 25px #00e5ff;
}

/* Labels */
.label{
    color:#94a3b8;
    font-size:15px;
}

/* Values */
.value{
    color:#00e5ff;
    font-size:32px;
    font-weight:bold;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:#07111f;
}

/* Button */
.stButton button{
    width:100%;
    background:linear-gradient(90deg,#06b6d4,#3b82f6);
    color:white;
    border:none;
    border-radius:12px;
    font-weight:bold;
}

.stButton button:hover{
    box-shadow:0 0 20px #00e5ff;
}

/* Number Input */
.stNumberInput input{
    background:#1e293b !important;
    color:white !important;
}

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown(
    "<div class='title'>🚀 Student Grade AI</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Advanced Grade Analysis Dashboard</div>",
    unsafe_allow_html=True
)

# ---------- INPUT ----------
marks = []

col1, col2 = st.columns([2,1])

with col1:
    for i in range(1, 6):
        mark = st.number_input(
            f"Subject {i}",
            min_value=0,
            max_value=100,
            value=50,
            step=1
        )
        marks.append(mark)

with col2:
    st.info("📊 Enter marks and generate AI grade analysis.")

# ---------- BUTTON ----------
if st.button("🚀 Calculate Grade"):

    total = sum(marks)
    percentage = total / 5

    if percentage >= 90:
        grade = "A+ 🌟"
    elif percentage >= 80:
        grade = "A 🎉"
    elif percentage >= 70:
        grade = "B 👍"
    elif percentage >= 60:
        grade = "C 🙂"
    elif percentage >= 50:
        grade = "D ⚠️"
    else:
        grade = "F ❌"

    st.write("")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(f"""
        <div class="card">
            <div class="label">TOTAL MARKS</div>
            <div class="value">{total}/500</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="card">
            <div class="label">PERCENTAGE</div>
            <div class="value">{percentage:.2f}%</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class="card">
            <div class="label">GRADE</div>
            <div class="value">{grade}</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.progress(int(percentage))
    st.success("✅ Analysis Completed Successfully")