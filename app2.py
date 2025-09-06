import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
import arabic_reshaper
from bidi.algorithm import get_display

# استخدام الخط "Traditional Arabic"
rcParams['font.family'] = 'Traditional Arabic'
rcParams['axes.unicode_minus'] = False

# ===== إضافة اللوقو =====
st.image("logo.png.jpg", width=300)  # تصغير اللوقو ليظهر بشكل عرضي نحيف

# العنوان الرئيسي
st.title("📊 تقرير شهر AUG")

# ===== قائمة جانبية للتنقل =====
menu = ["مستويات المتطوعين", "الإحصائيات"]
choice = st.sidebar.radio("اختر القسم:", menu)

# ===== قسم مستويات المتطوعين =====
if choice == "مستويات المتطوعين":
    st.header("📈 مستويات المتطوعين")
    
    # البيانات
    data_volunteers = {
        "المستوى": ["عام", "مهاري", "احترافي"],
        "عدد المتطوعين": [0, 7, 6]
    }
    df_volunteers = pd.DataFrame(data_volunteers)

    # عرض البيانات في جدول
    st.table(df_volunteers)

    # رسم بياني للمستويات
    fig, ax = plt.subplots(figsize=(8, 6))  
    ax.bar(df_volunteers["المستوى"], df_volunteers["عدد المتطوعين"])

    ax.set_xticklabels([get_display(arabic_reshaper.reshape(txt)) for txt in df_volunteers["المستوى"]], rotation=45, ha='right', fontsize=12)
    ax.set_xlabel('Level', fontsize=14, labelpad=15)  # تغيير النص إلى الإنجليزي هنا
    ax.set_ylabel('Number of Volunteers', fontsize=14, labelpad=15)  # تغيير النص إلى الإنجليزي هنا

    plt.tight_layout()  
    st.pyplot(fig)

# ===== قسم الإحصائيات =====
elif choice == "الإحصائيات":
    st.header("📊 إحصائيات شهر أغسطس")

    # البيانات الخاصة بالإحصائيات
    data_august = {
        "البيانات": ["عدد الفرص التطوعية", "عدد المتطوعين", "عدد الساعات", "العائد الاقتصادي", "عدد الذكور", "عدد الإناث"],
        "القيمة": [11, 13, 1215, 143000, 7, 6]
    }
    df_august = pd.DataFrame(data_august)

    # عرض البيانات في جدول
    st.table(df_august)

    # رسم بياني للفرص التطوعية
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(df_august["البيانات"], df_august["القيمة"])

    ax.set_xticklabels([get_display(arabic_reshaper.reshape(txt)) for txt in df_august["البيانات"]], rotation=45, ha='right', fontsize=12)
    ax.set_xlabel('Data', fontsize=14, labelpad=15)
    ax.set_ylabel('Value', fontsize=14, labelpad=15)

    plt.tight_layout()
    st.pyplot(fig)

    # ===== توزيع الذكور والإناث =====
    st.subheader("👦👧 توزيع الذكور والإناث")

    # رسم بياني لتوزيع الذكور والإناث
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.bar(["ذكور", "إناث"], [7, 6], color=['blue', 'pink'])

    ax.set_xticklabels([get_display(arabic_reshaper.reshape(txt)) for txt in ["ذكور", "إناث"]], rotation=45, ha='right', fontsize=12)
    ax.set_xlabel('Gender', fontsize=14, labelpad=15)
    ax.set_ylabel('Count', fontsize=14, labelpad=15)

    plt.tight_layout()
    st.pyplot(fig)

    # إضافة الأيقونات مع الأعداد
    st.write("👦 عدد الذكور:", 7)
    st.write("👧 عدد الإناث:", 6)

