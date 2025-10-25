import streamlit as st
import google.genai
from google.genai.types import Part
from google.genai.errors import ClientError

# ====================================================================
# إعداد واجهة STREAMLIT
# ====================================================================

st.set_page_config(page_title="Reports Summary", layout="centered")
st.title("Reports Summary")
st.markdown("This app uses the **Gemini API** to summarize")
st.divider()

# حقول الإدخال
col1, col2 = st.columns([3, 1])
with col1:
    report_input = st.text_area("Paste your report", label_visibility="collapsed", height=200, placeholder="Put your "
                                                                                                           "Report "
                                                                                                           "here..")
with col2:
    send_button = st.button("Send", use_container_width=True)

with st.expander("API Key"):
    api_key = st.text_input("Paste your Gemini API here", type="password")

# ====================================================================
# منطق معالجة Gemini API
# ====================================================================

# عرض رسالة التحذير فقط إذا كان المفتاح مفقوداً
if not api_key:
    st.warning("You need to paste your Gemini API key!")

# تنفيذ الكود فقط عند الضغط على زر "Send"
if send_button:

    # التحقق من المدخلات الأساسية
    if not api_key:
        st.error("Please enter your Gemini API Key before sending.")
        st.stop()  # إضافة st.stop() لمنع المزيد من التنفيذ في حال عدم وجود المفتاح

    st.success("Inputs received. Attempting to connect and summarize...")

    # 1. إنشاء العميل ومعالجة الأخطاء
    try:
        # إنشاء العميل
        client = google.genai.Client(api_key=api_key)

        # 2. صياغة البروم بت (نص فقط)
        prompt_text = (
                "قم بتلخيص هذا التقرير او المقال تلخيصا يوضح اهم النقاط و الأساسيات و الإحصاءات ألأساسية مع ذكر "
                "النقاط المحورية المهمة فقط" + report_input
        )

        # إعداد المحتوى (نص فقط) باستخدام الوسيطة المسماة
        contents = [
            Part.from_text(text=prompt_text)
        ]

        st.info("جاري إرسال الطلب...")

        # استدعاء الدالة عبر client.models
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=contents,
        )

        st.subheader("ملخص التقرير:")
        st.write(response.text)

    except ClientError as e:
        # ClientError هو الذي يحمل الكود 400 لمفتاح API غير الصالح
        st.error("Operation Failed! Client Error Encountered.")

        # لا نعرض تتبع الخطأ (Traceback) للمستخدم، بل فقط رسالة واضحة
        st.warning("⚠️ **API Key is invalid** or not configured correctly. Please check your key.")

        # يمكن تسجيل الخطأ الكامل في الكون سول للمطور
        print(f"DEBUG: ClientError captured: {e}")

    except Exception as e:
        # هذا يلتقط أي خطأ آخر غير ClientError (مثل مشكلات الشبكة أو أخطاء التنفيذ)
        st.error("Operation Failed! Please check the error details.")

        # عرض الخطأ غير المتوقع بطريقة Streamlit الصحيحة للمساعدة في التشخيص
        st.exception(e)
        st.warning(
            "An unexpected error occurred. The model might have some problems, please try again."
        )
