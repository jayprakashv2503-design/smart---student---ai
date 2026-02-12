import streamlit as st
import plotly.graph_objects as go
import time

st.set_page_config(page_title="Smart Student AI", layout="wide")

# ---------- Custom CSS ----------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
}
.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    margin-bottom: 10px;
}
.subtitle {
    text-align: center;
    font-size: 18px;
    color: #dcdcdc;
    margin-bottom: 30px;
}
.card {
    background: rgba(255,255,255,0.08);
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 0 30px rgba(0,0,0,0.4);
}
.footer {
    text-align: center;
    margin-top: 40px;
    font-size: 14px;
    color: #bbbbbb;
}
label {
    color: white !important;
    font-weight: 600 !important;
}
</style>
""", unsafe_allow_html=True)

# ---------- Title ----------
st.markdown('<div class="title">🤖 Smart Student AI Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI Powered Academic Performance Analyzer</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

# ---------- Input Section ----------
with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    study_hours = st.number_input("📚 Study Hours per Day", 0, 12, 4)
    attendance = st.number_input("🎓 Attendance Percentage", 0, 100, 75)
    previous_marks = st.number_input("📊 Previous Marks", 0, 100, 60)
    sleep_hours = st.number_input("😴 Sleep Hours", 0, 12, 6)
    screen_time = st.number_input("📱 Screen Time (Hours)", 0, 12, 4)

    st.markdown('</div>', unsafe_allow_html=True)

# ---------- Prediction Section ----------
with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("### 📊 AI Performance Meter")

    if st.button("🚀 Analyze Now"):

        with st.spinner("AI is analyzing lifestyle patterns..."):
            time.sleep(2)

            # Improved Scoring Logic (Out of 100)
            score = (
                study_hours * 6 +
                attendance * 0.3 +
                previous_marks * 0.4 +
                sleep_hours * 2 -
                screen_time * 4
            )

            score = max(0, min(100, score))  # Limit between 0–100

            # Gauge Chart
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=score,
                title={'text': "Performance Score"},
                gauge={
                    'axis': {'range': [0, 100]},
                    'bar': {'color': "#00ffcc"},
                    'steps': [
                        {'range': [0, 40], 'color': "#ff4d4d"},
                        {'range': [40, 70], 'color': "#ffa500"},
                        {'range': [70, 100], 'color': "#00cc66"},
                    ],
                }
            ))

            fig.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",
                font_color="white",
                height=350
            )

            st.plotly_chart(fig, use_container_width=True)

            # Creative Result Message
            if score >= 75:
                st.success("🔥 Outstanding Academic Potential Detected!")
            elif score >= 50:
                st.info("✨ Stable Performance — Improvement Possible!")
            else:
                st.error("⚠ Focus Required — Optimize Study Pattern!")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------- Footer ----------
st.markdown(
    '<div class="footer">Developed with ❤️ by Jayprakash Vishwakarma</div>',
    unsafe_allow_html=True
)