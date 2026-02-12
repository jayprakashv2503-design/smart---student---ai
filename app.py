import streamlit as st
st.markdown("""
    <style>
    div.stButton > button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        height: 50px;
        width: 100%;
        font-size: 18px;
    }

    div.stButton > button:hover {
        background-color: #45a049;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)
import plotly.graph_objects as go
import time

st.set_page_config(page_title="Smart Student AI", layout="wide")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
}
label {
    color: white !important;
    font-weight: 600 !important;
}
.footer {
    text-align: center;
    margin-top: 40px;
    font-size: 14px;
    color: #bbbbbb;
}
</style>
""", unsafe_allow_html=True)

st.title("🚀 Smart Student Growth Engine")
st.write("AI Powered Academic Motivation System")

col1, col2 = st.columns(2)

with col1:
    study = st.number_input("📚 Study Hours", 0, 12, 4)
    attendance = st.number_input("🎓 Attendance %", 0, 100, 75)
    previous = st.number_input("📊 Previous Marks", 0, 100, 60)
    sleep = st.number_input("😴 Sleep Hours", 0, 12, 6)
    screen = st.number_input("📱 Screen Time", 0, 12, 4)

with col2:

    if st.button("Analyze My Growth"):

        with st.spinner("Analyzing your growth potential..."):
            time.sleep(2)

            # Current Score
            current = (
                study * 6 +
                attendance * 0.3 +
                previous * 0.4 +
                sleep * 2 -
                screen * 4
            )

            current = max(0, min(100, current))

            # Ideal Score Calculation
            ideal = (
                8 * 6 +
                95 * 0.3 +
                85 * 0.4 +
                8 * 2 -
                1 * 4
            )

            ideal = max(0, min(100, ideal))

            gap = round(ideal - current, 2)

            # Gauge
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=current,
                title={'text': "Current Growth Score"},
                gauge={
                    'axis': {'range': [0, 100]},
                    'bar': {'color': "#00ffcc"},
                }
            ))

            fig.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",
                font_color="white",
                height=350
            )

            st.plotly_chart(fig, use_container_width=True)

            # Motivation Section
            st.subheader("📈 Growth Analysis")

            st.write(f"✨ Your Current Score: {round(current,2)} / 100")
            st.write(f"🎯 Your Growth Potential: +{gap} points possible!")

            if gap > 20:
                st.warning("🚀 Massive growth opportunity detected. Small habit changes can transform your results.")
            elif gap > 10:
                st.info("🔥 You're close to excellence. Fine-tuning daily habits will boost performance.")
            else:
                st.success("🏆 You're operating near peak performance. Maintain consistency!")

            st.subheader("🧠 Personalized Action Plan")

            if study < 6:
                st.write("📚 Increase study time by 1–2 hours daily.")
            if screen > 3:
                st.write("📱 Reduce screen time to improve focus.")
            if sleep < 7:
                st.write("😴 Improve sleep schedule for better productivity.")
            if attendance < 85:
                st.write("🎓 Maintain consistent attendance.")
            if previous < 70:
                st.write("📊 Revise weak subjects to strengthen foundation.")

            st.write("💡 Remember: Consistency beats intensity.")

st.markdown('<div class="footer">Developed by Jayprakash Vishwakarma</div>', unsafe_allow_html=True)

