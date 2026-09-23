import os
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

# -------------------------------------------------------------
# PRESENTATION CONFIGURATION & STYLING
# -------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIGURES_DIR = os.path.join(BASE_DIR, 'outputs', 'figures')
OUTPUT_PPTX = os.path.join(BASE_DIR, 'docs', 'Online_Food_Delivery_DAP_Final_Presentation.pptx')

# Color Palette Constants
COLOR_BG = RGBColor(248, 250, 252)        # Light Slate (#F8FAFC)
COLOR_CARD = RGBColor(255, 255, 255)      # White (#FFFFFF)
COLOR_BORDER = RGBColor(226, 232, 240)    # Slate 200 (#E2E8F0)
COLOR_PRIMARY = RGBColor(15, 23, 42)      # Deep Navy/Slate 900 (#0F172A)
COLOR_SECONDARY = RGBColor(71, 85, 105)   # Slate 600 (#475569)
COLOR_ACCENT = RGBColor(37, 99, 235)      # Blue 600 (#2563EB)
COLOR_ACCENT_BG = RGBColor(239, 246, 255) # Blue 50 (#EFF6FF)
COLOR_RED = RGBColor(225, 29, 72)         # Rose 600 (#E11D48)
COLOR_GREEN = RGBColor(5, 150, 105)       # Emerald 600 (#059669)
COLOR_DARK_BG = RGBColor(15, 23, 42)      # Deep Dark (#0F172A)

def create_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    def add_header(slide, title_text, step_badge=None, subtitle_text=None):
        # Background fill
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = COLOR_BG
        bg.line.fill.background()

        # Header bar
        header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.733), Inches(0.9))
        tf = header_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p = tf.paragraphs[0]
        if step_badge:
            run_badge = p.add_run()
            run_badge.text = f"[{step_badge}] "
            run_badge.font.name = 'Arial'
            run_badge.font.size = Pt(13)
            run_badge.font.bold = True
            run_badge.font.color.rgb = COLOR_ACCENT

        run_title = p.add_run()
        run_title.text = title_text
        run_title.font.name = 'Arial'
        run_title.font.size = Pt(20)
        run_title.font.bold = True
        run_title.font.color.rgb = COLOR_PRIMARY

        if subtitle_text:
            p2 = tf.add_paragraph()
            p2.space_before = Pt(3)
            run_sub = p2.add_run()
            run_sub.text = subtitle_text
            run_sub.font.name = 'Arial'
            run_sub.font.size = Pt(11)
            run_sub.font.color.rgb = COLOR_SECONDARY

        # Top Accent Strip
        strip = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.35), Inches(11.733), Inches(0.04))
        strip.fill.solid()
        strip.fill.fore_color.rgb = COLOR_ACCENT
        strip.line.fill.background()

        # Footer
        footer = slide.shapes.add_textbox(Inches(0.8), Inches(7.0), Inches(11.733), Inches(0.3))
        ftf = footer.text_frame
        fp = ftf.paragraphs[0]
        fp.text = "602 – Data Analytics Using Python (DAP) | Group 6 | Online Food Delivery Demand Forecasting & Peak Hour Regression"
        fp.font.name = 'Arial'
        fp.font.size = Pt(9)
        fp.font.color.rgb = RGBColor(148, 163, 184)

    # -------------------------------------------------------------------------
    # SLIDE 1: Title Slide (Dark Theme for Executive Impact)
    # -------------------------------------------------------------------------
    slide1 = prs.slides.add_slide(blank_layout)
    bg1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = COLOR_DARK_BG
    bg1.line.fill.background()

    # Title Card Accent
    card1 = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.2), Inches(1.0), Inches(10.933), Inches(5.5))
    card1.fill.solid()
    card1.fill.fore_color.rgb = RGBColor(30, 41, 59)
    card1.line.color.rgb = RGBColor(51, 65, 85)
    card1.line.width = Pt(1.5)

    tb1 = slide1.shapes.add_textbox(Inches(1.6), Inches(1.3), Inches(10.133), Inches(4.8))
    tf1 = tb1.text_frame
    tf1.word_wrap = True

    p = tf1.paragraphs[0]
    r = p.add_run()
    r.text = "TYBCA SEMESTER-6 | FINAL ACADEMIC PROJECT PRESENTATION"
    r.font.name = 'Arial'
    r.font.size = Pt(12)
    r.font.bold = True
    r.font.color.rgb = RGBColor(56, 189, 248)

    p = tf1.add_paragraph()
    p.space_before = Pt(12)
    r = p.add_run()
    r.text = "Online Food Delivery Demand Forecasting &\nPeak Hour Regression Model"
    r.font.name = 'Arial'
    r.font.size = Pt(28)
    r.font.bold = True
    r.font.color.rgb = RGBColor(255, 255, 255)

    p = tf1.add_paragraph()
    p.space_before = Pt(14)
    r = p.add_run()
    r.text = "A Complete 15-Step Academic DAP Pipeline with Supervised Regression & Classification Modeling"
    r.font.name = 'Arial'
    r.font.size = Pt(14)
    r.font.color.rgb = RGBColor(203, 213, 225)

    p = tf1.add_paragraph()
    p.space_before = Pt(24)
    r = p.add_run()
    r.text = "• Subject: 602 – Data Analytics Using Python (DAP)\n• Group No: 6\n• Domain: Food, E-Commerce & Consumer Analytics\n• Reference Standard: DAP Curriculum Benchmark (Zomato Reference Architecture)"
    r.font.name = 'Arial'
    r.font.size = Pt(12)
    r.font.color.rgb = RGBColor(148, 163, 184)

    # Helper function for 2-column cards
    def add_two_column_cards(slide, left_title, left_bullets, right_title, right_bullets):
        # Left Card
        l_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.1))
        l_card.fill.solid()
        l_card.fill.fore_color.rgb = COLOR_CARD
        l_card.line.color.rgb = COLOR_BORDER
        l_card.line.width = Pt(1)

        l_tb = slide.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.2), Inches(4.7))
        l_tf = l_tb.text_frame
        l_tf.word_wrap = True
        p = l_tf.paragraphs[0]
        r = p.add_run()
        r.text = left_title
        r.font.name = 'Arial'
        r.font.size = Pt(16)
        r.font.bold = True
        r.font.color.rgb = COLOR_ACCENT

        for b in left_bullets:
            p = l_tf.add_paragraph()
            p.space_before = Pt(8)
            r = p.add_run()
            r.text = b
            r.font.name = 'Arial'
            r.font.size = Pt(12)
            r.font.color.rgb = COLOR_PRIMARY

        # Right Card
        r_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.1))
        r_card.fill.solid()
        r_card.fill.fore_color.rgb = COLOR_CARD
        r_card.line.color.rgb = COLOR_BORDER
        r_card.line.width = Pt(1)

        r_tb = slide.shapes.add_textbox(Inches(7.0), Inches(1.8), Inches(5.3), Inches(4.7))
        r_tf = r_tb.text_frame
        r_tf.word_wrap = True
        p = r_tf.paragraphs[0]
        r = p.add_run()
        r.text = right_title
        r.font.name = 'Arial'
        r.font.size = Pt(16)
        r.font.bold = True
        r.font.color.rgb = COLOR_ACCENT

        for b in right_bullets:
            p = r_tf.add_paragraph()
            p.space_before = Pt(8)
            r = p.add_run()
            r.text = b
            r.font.name = 'Arial'
            r.font.size = Pt(12)
            r.font.color.rgb = COLOR_PRIMARY

    # Helper function for Image + Analysis Slide
    def add_image_slide(slide, image_filename, takeaways_title, takeaways_list, key_metric_box=None):
        img_path = os.path.join(FIGURES_DIR, image_filename)
        if os.path.exists(img_path):
            slide.shapes.add_picture(img_path, Inches(0.8), Inches(1.6), width=Inches(6.4))
        
        # Right Analysis Card
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.5), Inches(1.6), Inches(5.0), Inches(5.1))
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD
        card.line.color.rgb = COLOR_BORDER
        card.line.width = Pt(1)

        tb = slide.shapes.add_textbox(Inches(7.7), Inches(1.8), Inches(4.6), Inches(4.7))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        r = p.add_run()
        r.text = takeaways_title
        r.font.name = 'Arial'
        r.font.size = Pt(15)
        r.font.bold = True
        r.font.color.rgb = COLOR_ACCENT

        for item in takeaways_list:
            p = tf.add_paragraph()
            p.space_before = Pt(8)
            r = p.add_run()
            r.text = item
            r.font.name = 'Arial'
            r.font.size = Pt(11)
            r.font.color.rgb = COLOR_PRIMARY

        if key_metric_box:
            p = tf.add_paragraph()
            p.space_before = Pt(12)
            r = p.add_run()
            r.text = f"KEY TAKEAWAY: {key_metric_box}"
            r.font.name = 'Arial'
            r.font.size = Pt(11)
            r.font.bold = True
            r.font.color.rgb = COLOR_RED

    # -------------------------------------------------------------------------
    # SLIDE 2: Project Introduction & Domain Overview
    # -------------------------------------------------------------------------
    slide2 = prs.slides.add_slide(blank_layout)
    add_header(slide2, "Project Introduction & Domain Overview", "Overview", "Food, E-Commerce & Consumer Analytics Domain")
    add_two_column_cards(
        slide2,
        "Industry & Domain Background",
        [
            "• Massive Industry Growth: Rapid adoption of online food delivery apps (Zomato, Swiggy, UberEats) has created complex, high-velocity operational networks.",
            "• Dual Operational Dimensions: Success depends on understanding when consumer demand peaks and accurately estimating how long delivery fulfillment will take.",
            "• Hyper-Local Volatility: Demand varies dramatically across hours of the day, traffic conditions, courier availability, and geographical transit distances."
        ],
        "Academic Analytics Motivation",
        [
            "• Structured DAP Methodology: Implements the 15-step Data Analytics using Python framework to extract actionable insights from raw operational logs.",
            "• Machine Learning Integration: Integrates Multiple Linear Regression for duration forecasting and Logistic Regression for peak demand classification.",
            "• End-to-End Integrity: Uses a real benchmark dataset of 45,593 verified delivery records with zero simulated data or fabricated metrics."
        ]
    )

    # -------------------------------------------------------------------------
    # SLIDE 3: Problem Statement
    # -------------------------------------------------------------------------
    slide3 = prs.slides.add_slide(blank_layout)
    add_header(slide3, "Problem Statement & Operational Challenges", "Context", "Identifying Delivery Bottlenecks & Demand Spikes")
    add_two_column_cards(
        slide3,
        "Key Operational Bottlenecks",
        [
            "• Severe Peak Hour Congestion: Concentrated consumer order surges during lunch and dinner overwhelm delivery courier capacity.",
            "• Unpredictable Delivery Delays: Unforeseen traffic jams, severe weather, and multiple concurrent drop-offs lead to late deliveries and customer churn.",
            "• Inaccurate Static ETA Estimates: Rigid, distance-only time calculations fail to account for real-time traffic levels, courier ratings, or vehicle conditions."
        ],
        "Core Analytics Questions",
        [
            "1. When do peak order demand windows occur, and what share of total volume do they represent?",
            "2. How significantly do distance, road traffic density, and courier factors impact delivery duration?",
            "3. Can Multiple Linear Regression reliably predict continuous delivery times on unseen orders?",
            "4. Can Logistic Regression accurately classify incoming orders into peak vs. off-peak windows?"
        ]
    )

    # -------------------------------------------------------------------------
    # SLIDE 4: Project Objectives & Scope
    # -------------------------------------------------------------------------
    slide4 = prs.slides.add_slide(blank_layout)
    add_header(slide4, "Project Objectives & Scope", "Objectives", "Analytical & Machine Learning Deliverables")
    add_two_column_cards(
        slide4,
        "Primary Analytical Goals",
        [
            "• Data Cleaning & Feature Engineering: Parse operational formats, compute Haversine spatial distance (km), and engineer temporal order metrics.",
            "• Exploratory Data Analysis: Perform comprehensive Univariate, Bivariate, and Multivariate EDA to profile customer demand behavior.",
            "• Statistical Imputation: Handle missing values and audit extreme outliers following academic curriculum guidelines."
        ],
        "Predictive Modeling Deliverables",
        [
            "• Supervised Regression Model: Train `LinearRegression` on 80/20 train-test partition to forecast delivery fulfillment duration.",
            "• Supervised Classification Model: Train `LogisticRegression` to classify orders into Peak vs. Non-Peak windows.",
            "• Rigorous Model Evaluation: Calculate MSE, MAE, R², Confusion Matrix, and Underfitting/Overfitting diagnostics.",
            "• Actionable Recommendations: Propose dynamic courier pre-allocation and surge buffer policies for food delivery platforms."
        ]
    )

    # -------------------------------------------------------------------------
    # SLIDE 5: Academic Source of Truth & DAP Workflow
    # -------------------------------------------------------------------------
    slide5 = prs.slides.add_slide(blank_layout)
    add_header(slide5, "Academic Source of Truth & DAP 15-Step Workflow", "Framework", "VNSGU 602 DAP Curriculum Reference Alignment")
    add_two_column_cards(
        slide5,
        "The 15 Standard DAP Steps",
        [
            "• Step 1: Python Libraries Import\n• Step 2: Load Data & Create DataFrame\n• Step 3: Data Understanding & Types\n• Step 4: Data Spread & Preparation\n• Step 5: Check Missing & Outliers\n• Step 6: Handle Missing & Outliers\n• Step 7: EDA Univariate Analysis\n• Step 8: EDA Bivariate Analysis",
            "• Step 9: EDA Multivariate Analysis\n• Step 10: Regression Analysis\n• Step 11: Regression Model Evaluation\n• Step 12: Classification Model\n• Step 13: Classification Evaluation\n• Step 14: Underfitting / Overfitting\n• Step 15: Conclusion & Insights"
        ],
        "100-Marks Marking Scheme Alignment",
        [
            "• Data Understanding & Cleaning (20 Marks): Dataset loading, type casting, string cleaning, mean imputation.",
            "• EDA & Visualization (25 Marks): Min. 5 graphs across univariate, bivariate, multivariate with written conclusions.",
            "• Regression & ML Concepts (25 Marks): Train-test split (80/20), random state, feature coefficients, bias-variance analysis.",
            "• Model Evaluation (15 Marks): MSE, MAE, R², 45° actual vs predicted line, classification accuracy, confusion matrix.",
            "• Viva & Presentation (15 Marks): Structured format, verified outputs, academic defense readiness."
        ]
    )

    # -------------------------------------------------------------------------
    # SLIDE 6: Dataset Description & Characteristics
    # -------------------------------------------------------------------------
    slide6 = prs.slides.add_slide(blank_layout)
    add_header(slide6, "Dataset Overview & Characteristics", "Data", "Benchmark Real Food Delivery Operations Dataset")
    add_two_column_cards(
        slide6,
        "Dataset Specifications",
        [
            "• Total Raw Records: 45,593 verified customer orders.",
            "• Total Features: 20 raw attributes $\\rightarrow$ 28 engineered features.",
            "• Data Source: Benchmark Multi-City Food Delivery Logistics Dataset (merged orders, courier, and spatial tables).",
            "• Geographical Coverage: Multi-hub metropolitan & urban zones.",
            "• Continuous Target ($y_1$): `delivery_time_min` (Mean: 26.30 min, Range: 10–54 min).",
            "• Classification Target ($y_2$): `is_peak_hour` (Binary 0/1 indicator)."
        ],
        "Feature Categorization",
        [
            "• Temporal Features: `Order_Date`, `Time_Orderd`, `Time_Order_picked`, `order_hour`, `day_of_week`, `is_weekend`.",
            "• Spatial Features: `Restaurant_latitude/longitude`, `Delivery_location_latitude/longitude`, `distance_km`.",
            "• Operational Features: `Road_traffic_density`, `Weatherconditions`, `Vehicle_condition`, `multiple_deliveries`.",
            "• Human/Courier Features: `Delivery_person_Age`, `Delivery_person_Ratings`."
        ]
    )

    # -------------------------------------------------------------------------
    # SLIDE 7: Step 1 — Python Libraries & Environment Setup
    # -------------------------------------------------------------------------
    slide7 = prs.slides.add_slide(blank_layout)
    add_header(slide7, "Python Libraries & Environment Setup", "Step 1", "Core Academic Stack for Analytics & Machine Learning")
    add_two_column_cards(
        slide7,
        "Libraries & Purpose",
        [
            "• `pandas`: DataFrame manipulation, time-series parsing, cross-tabulation.",
            "• `numpy`: Mathematical calculations, array vectorization, Haversine spherical trigonometry.",
            "• `matplotlib.pyplot`: Foundational charting, figure structuring, 45-degree diagonal reference lines.",
            "• `seaborn`: Statistical distributions, heatmaps, categorical boxplots, regression trendlines."
        ],
        "Machine Learning Suite (`scikit-learn`)",
        [
            "• `sklearn.model_selection.train_test_split`: Deterministic 80/20 data partitioning (`random_state=42`).",
            "• `sklearn.linear_model.LinearRegression`: Ordinary Least Squares (OLS) regression modeling.",
            "• `sklearn.linear_model.LogisticRegression`: Maximum Likelihood binary classification modeling.",
            "• `sklearn.metrics`: MSE, MAE, R² Score, Accuracy Score, Confusion Matrix, Classification Report."
        ]
    )

    # -------------------------------------------------------------------------
    # SLIDE 8: Step 2 & 3 — Data Loading & Understanding
    # -------------------------------------------------------------------------
    slide8 = prs.slides.add_slide(blank_layout)
    add_header(slide8, "Data Loading & Structural Inspection", "Step 2 & 3", "Verifying Data Types, Dimensions & Summary Statistics")
    add_two_column_cards(
        slide8,
        "Step 2: DataFrame Creation",
        [
            "• Loading: `pd.read_csv('../data/raw/food_delivery_raw.csv')`.",
            "• Row Count: Exactly 45,593 rows loaded into memory.",
            "• Column Count: 20 initial attributes.",
            "• Shape Verification: `.shape` confirmed `(45593, 20)`.",
            "• Top/Bottom Records: Inspected via `.head()` and `.tail()` to ensure zero truncation or file corruption."
        ],
        "Step 3: Understanding Structure & Summary",
        [
            "• Data Types: 10 numerical features, 13 categorical strings, 1 datetime object.",
            "• Summary Statistics (`.describe()`):",
            "  - Courier Age: Mean 29.56 years (Range: 15–50).",
            "  - Courier Ratings: Mean 4.63 / 5.0 (Range: 1.0–6.0).",
            "  - Delivery Duration: Mean 26.30 min, Std 9.38 min.",
            "  - Delivery Distance: Mean 9.74 km (Max capped at 50 km)."
        ]
    )

    # -------------------------------------------------------------------------
    # SLIDE 9: Step 4 — Data Spread & Preparation (Feature Engineering)
    # -------------------------------------------------------------------------
    slide9 = prs.slides.add_slide(blank_layout)
    add_header(slide9, "Data Spread, Cleaning & Feature Engineering", "Step 4", "String Cleaning, Time Parsing & Haversine Distance Calculation")
    add_two_column_cards(
        slide9,
        "Cleaning String & Format Artifacts",
        [
            "• Delivery Time Cleaning: Converted `'(min) 24'` $\\rightarrow$ `24.0` numeric float (analogous to `handleRate` in reference Zomato notebook).",
            "• Weather String Cleaning: Cleaned `'conditions Fog'` $\\rightarrow$ `'Fog'`.",
            "• Whitespace Stripping: Stripped whitespace across all categorical text columns.",
            "• Missing Representation: Replaced `'NaN'`, `'null'`, empty strings with standard `np.nan`."
        ],
        "Engineered Mathematical Features",
        [
            "• Haversine Distance (km): Computed geodesic distance from GPS pairs using spherical trigonometry:",
            "  $$d = 2r \\arcsin\\left(\\sqrt{\\sin^2(\\Delta\\phi/2) + \\cos\\phi_1\\cos\\phi_2\\sin^2(\\Delta\\lambda/2)}\\right)$$",
            "• Temporal Parsing: Extracted `order_hour` (0–23), `day_of_week`, and `is_weekend` flag.",
            "• Peak Hour Indicator: Derived `is_peak_hour = 1` for lunch (12–14h) & dinner (18–23h) demand windows."
        ]
    )

    # -------------------------------------------------------------------------
    # SLIDE 10: Step 5 & 6 — Missing Data & Outlier Handling
    # -------------------------------------------------------------------------
    slide10 = prs.slides.add_slide(blank_layout)
    add_header(slide10, "Missing Data Imputation & Outlier Diagnostics", "Step 5 & 6", "Academic Imputation Standard & Domain Validation")
    add_two_column_cards(
        slide10,
        "Step 5: Missing Data & Outliers Audit",
        [
            "• Missing Values Audit: Identified nulls in `Delivery_person_Age`, `Delivery_person_Ratings`, `multiple_deliveries`, `distance_km`.",
            "• Outlier Detection: Boxplot inspection showed delivery times ranging between 10 to 54 minutes.",
            "• Outlier Decision: Values > 45 minutes reflect genuine adverse events (traffic jams, heavy rain) rather than measurement errors; preserved to retain natural real-world variance."
        ],
        "Step 6: Systematic Imputation",
        [
            "• Numerical Imputation: Followed curriculum standard via column mean replacement:",
            "  `df.fillna(df.mean(numeric_only=True), inplace=True)`",
            "• Categorical Imputation: Mode replacement for missing traffic density, weather condition, and city type.",
            "• Final Audit: Verified 0 remaining missing values across all 45,593 records."
        ]
    )

    # -------------------------------------------------------------------------
    # SLIDE 11: Step 7 — Univariate EDA: Delivery Time Distribution
    # -------------------------------------------------------------------------
    slide11 = prs.slides.add_slide(blank_layout)
    add_header(slide11, "Univariate EDA: Delivery Duration Distribution", "Step 7", "Analyzing Target Spread & Central Tendency")
    add_image_slide(
        slide11,
        "01_delivery_time_distribution.png",
        "Statistical Distribution Summary",
        [
            "• Symmetric Bell-Shaped Curve: Delivery durations exhibit a clean, near-normal distribution.",
            "• Central Metrics: Mean delivery time is 26.3 minutes; median is 26.0 minutes.",
            "• Operational Spread: Interquartile range spans 19 to 32 minutes, with standard orders completing within 15–40 minutes.",
            "• Tail Events: Deliveries extending past 45 minutes correspond directly to severe traffic jams and multiple concurrent stops."
        ],
        "Mean Delivery Time = 26.3 min | Median = 26.0 min"
    )

    # -------------------------------------------------------------------------
    # SLIDE 12: Step 7 — Univariate EDA: Hourly Demand Pattern
    # -------------------------------------------------------------------------
    slide12 = prs.slides.add_slide(blank_layout)
    add_header(slide12, "Univariate EDA: Hourly Order Demand Pattern", "Step 7", "Identifying 24-Hour Consumer Ordering Cycles")
    add_image_slide(
        slide12,
        "02_hourly_demand_distribution.png",
        "24-Hour Demand Observations",
        [
            "• Bimodal Demand Peaks: Clear consumer ordering surges occur during lunch (12:00–14:00) and dinner (18:00–22:00).",
            "• Dominant Evening Peak: 19:00 is the single busiest hour (4,595 orders), closely followed by 18:00 (4,480 orders) and 20:00 (4,230 orders).",
            "• Secondary Lunch Surge: Moderate peak at 13:00 (~1,850 orders).",
            "• Off-Peak Troughs: Minimal ordering between 00:00–07:00 and late afternoon (15:00–17:00)."
        ],
        "Peak Demand Windows: 12-14h (Lunch) & 18-22h (Dinner)"
    )

    # -------------------------------------------------------------------------
    # SLIDE 13: Step 7 — Univariate EDA: Peak vs. Non-Peak Split
    # -------------------------------------------------------------------------
    slide13 = prs.slides.add_slide(blank_layout)
    add_header(slide13, "Univariate EDA: Peak vs. Non-Peak Order Volume Split", "Step 7", "Quantifying Platform Traffic Distribution")
    add_image_slide(
        slide13,
        "03_peak_vs_nonpeak_demand.png",
        "Traffic Distribution Breakdown",
        [
            "• Peak Window Concentration: 65.48% of all platform orders (29,853 orders) occur during designated peak hours.",
            "• Off-Peak Window: 34.52% of platform volume (15,740 orders) is spread across off-peak periods.",
            "• Fleet Imbalance: Operational pressure on delivery fleets is concentrated in less than 9 operating hours daily.",
            "• Scheduling Target: Justifies the binary classification problem (`is_peak_hour`) for dynamic courier surge pricing."
        ],
        "65.5% of Total Daily Orders Occur During Peak Hours"
    )

    # -------------------------------------------------------------------------
    # SLIDE 14: Step 7 — Univariate EDA: Weekly Demand Trends
    # -------------------------------------------------------------------------
    slide14 = prs.slides.add_slide(blank_layout)
    add_header(slide14, "Univariate EDA: Weekly Demand Trends", "Step 7", "Analyzing Day-of-Week Consumer Ordering Behavior")
    add_image_slide(
        slide14,
        "04_day_of_week_demand.png",
        "Weekly Order Dynamics",
        [
            "• Steady Weekday Baseline: Consistent order volumes from Monday through Thursday (~6,200–6,400 orders/day).",
            "• Weekend Elevation: Significant volume expansion on Friday, Saturday, and Sunday (~6,800+ orders/day).",
            "• Friday Dinner Spike: Highest single-day order density occurs on Friday evenings as weekend leisure ordering begins.",
            "• Operational Insight: Delivery partner incentives and fleet availability must scale by +15% over weekends."
        ],
        "Weekend Demand Surges Require Dynamic Staffing"
    )

    # -------------------------------------------------------------------------
    # SLIDE 15: Step 8 — Bivariate EDA: Distance vs. Delivery Duration
    # -------------------------------------------------------------------------
    slide15 = prs.slides.add_slide(blank_layout)
    add_header(slide15, "Bivariate EDA: Distance vs. Delivery Duration", "Step 8", "Quantifying Transit Distance & Traffic Congestion Interactions")
    add_image_slide(
        slide15,
        "05_distance_vs_delivery_time.png",
        "Bivariate Relationship Insights",
        [
            "• Positive Linear Correlation: Delivery duration increases steadily with geographical distance in km.",
            "• Traffic Stratification: Points stratified by traffic level (Low, Medium, High, Jam) demonstrate clear vertical shift.",
            "• Traffic Delays Outweigh Distance: Short deliveries (3–5 km) in severe Jam traffic frequently take longer than long deliveries (15 km) in Low traffic.",
            "• Confirms Multivariable Need: Distance alone cannot predict delivery duration; traffic density is a vital predictor."
        ],
        "Traffic Level is as Critical as Physical Transit Distance"
    )

    # -------------------------------------------------------------------------
    # SLIDE 16: Step 8 — Bivariate EDA: Traffic Density Impact
    # -------------------------------------------------------------------------
    slide16 = prs.slides.add_slide(blank_layout)
    add_header(slide16, "Bivariate EDA: Delivery Duration by Traffic Level", "Step 8", "Boxplot Spread Across Traffic Congestion Categories")
    add_image_slide(
        slide16,
        "06_traffic_density_boxplot.png",
        "Traffic Density Analysis",
        [
            "• Low Traffic: Median delivery time = 21.0 minutes (IQR: 15–26 min).",
            "• Medium Traffic: Median delivery time = 26.0 minutes (IQR: 20–31 min).",
            "• High Traffic: Median delivery time = 29.0 minutes (IQR: 23–35 min).",
            "• Jam Conditions: Median delivery time = 35.0 minutes (IQR: 28–42 min).",
            "• Congestion Penalty: Severe traffic jams add an average delay of +14.0 minutes over free-flowing traffic."
        ],
        "Traffic Jam Adds +14 Minutes Average Delivery Delay"
    )

    # -------------------------------------------------------------------------
    # SLIDE 17: Step 9 — Multivariate EDA: Order Type & Traffic Heatmap
    # -------------------------------------------------------------------------
    slide17 = prs.slides.add_slide(blank_layout)
    add_header(slide17, "Multivariate EDA: Mean Delivery Time Cross-Tab", "Step 9", "Two-Way Pivot Table of Order Type vs. Traffic Density")
    add_image_slide(
        slide17,
        "07_multivariate_pivot_heatmap.png",
        "Multivariate Pivot Findings",
        [
            "• Cross-Tab Dimensions: Evaluates average delivery duration across 4 Order Types (Buffet, Drinks, Meal, Snack) and 4 Traffic Levels.",
            "• Uniform Meal Preparation: Baseline delivery times across all 4 meal types are nearly identical (~25.8–26.5 min).",
            "• Universal Traffic Vulnerability: Under Jam conditions, delivery times increase to ~35.2 min regardless of whether the order is a Snack or a Buffet.",
            "• Takeaway: External logistical factors dominate internal kitchen preparation times."
        ],
        "Traffic Delays Affect All Order Types Uniformly (~35 min)"
    )

    # -------------------------------------------------------------------------
    # SLIDE 18: Step 9 — Multivariate EDA: Feature Correlation Matrix
    # -------------------------------------------------------------------------
    slide18 = prs.slides.add_slide(blank_layout)
    add_header(slide18, "Multivariate EDA: Numerical Correlation Matrix", "Step 9", "Evaluating Inter-Feature Statistical Correlations")
    add_image_slide(
        slide18,
        "08_correlation_heatmap.png",
        "Correlation Insights",
        [
            "• Strong Positive Drivers of Delivery Time:",
            "  - `multiple_deliveries` (+0.38): Major delay factor.",
            "  - `distance_km` (+0.30): Direct physical transit driver.",
            "  - `Delivery_person_Age` (+0.29): Moderate positive relationship.",
            "• Strong Negative Drivers (Efficiency):",
            "  - `Delivery_person_Ratings` (-0.36): Highly rated riders deliver faster.",
            "  - `Vehicle_condition` (-0.24): Maintained vehicles reduce transit delay."
        ],
        "Rider Ratings & Vehicle Condition Accelerate Deliveries"
    )

    # -------------------------------------------------------------------------
    # SLIDE 19: Step 10 — Regression Modeling Architecture
    # -------------------------------------------------------------------------
    slide19 = prs.slides.add_slide(blank_layout)
    add_header(slide19, "Regression Modeling Architecture", "Step 10", "Forecasting Operational Delivery Duration (Minutes)")
    add_two_column_cards(
        slide19,
        "Problem Formulation",
        [
            "• Objective: Predict continuous delivery duration (`delivery_time_min`) from operational and environmental features.",
            "• Mathematical Equation:",
            "  $$\\hat{y} = \\beta_0 + \\sum_{i=1}^{p} \\beta_i X_i$$",
            "• Feature Matrix ($X$): Distance, hour, courier age, ratings, vehicle condition, multiple deliveries, traffic dummies, weather dummies.",
            "• Zero Data Leakage: Order IDs and raw target derived metrics excluded."
        ],
        "Training & Validation Setup",
        [
            "• Train-Test Partition: 80% Training ($N = 36,474$), 20% Testing ($N = 9,119$).",
            "• Reproducibility: Defined `random_state = 42`.",
            "• Algorithm: Scikit-learn `LinearRegression()` with Ordinary Least Squares (OLS) estimation.",
            "• Model Artifact: Serialized to `outputs/models/linear_regression_demand.joblib`."
        ]
    )

    # -------------------------------------------------------------------------
    # SLIDE 20: Step 10 — Regression Coefficients & Feature Importances
    # -------------------------------------------------------------------------
    slide20 = prs.slides.add_slide(blank_layout)
    add_header(slide20, "Regression Feature Coefficients & Interpretation", "Step 10", "Quantifying the Impact of Key Operational Predictors")
    add_two_column_cards(
        slide20,
        "Top Delay Factors (+ve Coefficients)",
        [
            "• `multiple_deliveries` ($\\beta = +3.4409$): Each additional batch stop adds ~3.44 minutes to delivery time.",
            "• `traffic_Jam` ($\\beta = +1.0032$): Severe congestion consistently delays delivery schedules.",
            "• `Delivery_person_Age` ($\\beta = +0.4176$): Older courier age exhibits slightly longer fulfillment times.",
            "• `distance_km` ($\\beta = +0.3667$): Each additional kilometer adds ~0.37 min (22 seconds) transit time."
        ],
        "Top Speed Factors (-ve Coefficients)",
        [
            "• `Delivery_person_Ratings` ($\\beta = -7.1816$): Top-rated couriers complete orders ~7.18 minutes faster per rating point.",
            "• `weather_Sunny` ($\\beta = -6.7157$): Clear weather accelerates deliveries by ~6.72 minutes vs. adverse weather.",
            "• `traffic_Low` ($\\beta = -6.5874$): Free-flowing traffic saves ~6.59 minutes over baseline.",
            "• `Vehicle_condition` ($\\beta = -2.3176$): Well-maintained vehicles reduce transit delay by ~2.32 minutes per condition tier."
        ]
    )

    # -------------------------------------------------------------------------
    # SLIDE 21: Step 11 — Regression Model Evaluation Metrics
    # -------------------------------------------------------------------------
    slide21 = prs.slides.add_slide(blank_layout)
    add_header(slide21, "Regression Model Evaluation Metrics", "Step 11", "Quantitative Assessment of Forecasting Accuracy")
    add_two_column_cards(
        slide21,
        "Calculated Evaluation Metrics",
        [
            "• Mean Squared Error (MSE):",
            "  - Training Set: 40.1144",
            "  - Testing Set: 39.6322 (Low residual variance)",
            "• Mean Absolute Error (MAE):",
            "  - Training Set: 5.0236 min",
            "  - Testing Set: 4.9990 min (Average error < 5 minutes)",
            "• Coefficient of Determination ($R^2$ Score):",
            "  - Training Set: 0.5449",
            "  - Testing Set: 0.5480 (54.80% variance explained)"
        ],
        "Academic Metric Interpretation",
        [
            "• MAE Significance: An MAE of ~5.0 minutes means that for an average 26-minute delivery, predictions deviate by less than 5 minutes on unseen real orders.",
            "• $R^2$ Performance: Explaining 54.80% of variance in urban logistics—where traffic and weather are highly noisy—demonstrates solid linear model fit.",
            "• Generalization Consistency: Test MSE is slightly lower than Train MSE, confirming zero overfitting."
        ]
    )

    # -------------------------------------------------------------------------
    # SLIDE 22: Step 11 — Actual vs. Predicted Scatter Plot (45° Line)
    # -------------------------------------------------------------------------
    slide22 = prs.slides.add_slide(blank_layout)
    add_header(slide22, "Regression Evaluation: Actual vs. Predicted Plot", "Step 11", "Mandatory DAP 45-Degree Reference Diagonal Validation")
    add_image_slide(
        slide22,
        "09_actual_vs_predicted_regression.png",
        "Scatter Plot Diagnostics",
        [
            "• DAP Requirement: Evaluates test predictions against actual values along the red 45° dashed reference line ($y=x$).",
            "• Unbiased Alignment: Data points are distributed symmetrically along the 45-degree diagonal across the 10–50 minute range.",
            "• Stable Error Bounds: No extreme horn-shaped heteroskedasticity; residual variance remains consistent across low and high delivery times.",
            "• Residual Error: Visualized in `outputs/figures/10_regression_residuals_distribution.png` as a zero-centered normal distribution."
        ],
        "Model Predictions Track Actual Delivery Durations Accurately"
    )

    # -------------------------------------------------------------------------
    # SLIDE 23: Step 12 — Classification Modeling (Peak Hour Prediction)
    # -------------------------------------------------------------------------
    slide23 = prs.slides.add_slide(blank_layout)
    add_header(slide23, "Classification Modeling: Peak Hour Prediction", "Step 12", "Supervised Logistic Regression for Dynamic Demand Windows")
    add_two_column_cards(
        slide23,
        "Classification Formulation",
        [
            "• Objective: Classify whether an order falls into a Peak Demand Window ($1$) vs. Off-Peak Period ($0$).",
            "• Empirical Target ($y$):",
            "  $$y = \\begin{cases} 1, & \\text{if Hour} \\in [12, 13, 14, 18, 19, 20, 21, 22, 23] \\\\ 0, & \\text{otherwise} \\end{cases}$$",
            "• Business Purpose: Trigger automated fleet surge alerts and dynamic courier incentive bonuses."
        ],
        "Model Setup & Features",
        [
            "• Features ($X$): Delivery duration, distance, courier age, rating, vehicle condition, multiple deliveries, traffic dummies, weather dummies.",
            "• Stratified 80/20 Partition: $N = 36,474$ Train / $N = 9,119$ Test.",
            "• Algorithm: `LogisticRegression(max_iter=1000, random_state=42)`.",
            "• Model Artifact: Serialized to `outputs/models/logistic_regression_peak_hour.joblib`."
        ]
    )

    # -------------------------------------------------------------------------
    # SLIDE 24: Step 13 — Classification Evaluation & Confusion Matrix
    # -------------------------------------------------------------------------
    slide24 = prs.slides.add_slide(blank_layout)
    add_header(slide24, "Classification Evaluation & Confusion Matrix", "Step 13", "Accuracy, Precision, Recall & Heatmap Analysis")
    add_image_slide(
        slide24,
        "11_classification_confusion_matrix.png",
        "Classification Performance Metrics",
        [
            "• Testing Accuracy: 81.66% on unseen test instances (Training Accuracy: 81.84%).",
            "• Confusion Matrix Breakdown ($N = 9,119$):",
            "  - True Negatives (Non-Peak Correct): 2,314",
            "  - False Positives: 834",
            "  - False Negatives: 838",
            "  - True Positives (Peak Hours Correct): 5,133",
            "• Peak Hour Recall: 85.97% ($5,133 / 5,971$)",
            "• Peak Hour Precision: 86.02% ($5,133 / 5,967$)"
        ],
        "81.66% Test Accuracy | 86.0% Peak Hour Detection Recall"
    )

    # -------------------------------------------------------------------------
    # SLIDE 25: Step 14 — Underfitting vs. Overfitting Diagnostics
    # -------------------------------------------------------------------------
    slide25 = prs.slides.add_slide(blank_layout)
    add_header(slide25, "Underfitting vs. Overfitting Diagnostics", "Step 14", "Rigorous Train vs. Test Performance & Generalization Analysis")
    add_two_column_cards(
        slide25,
        "Performance Generalization Table",
        [
            "• Linear Regression ($R^2$):",
            "  - Train $R^2 = 0.5449$ | Test $R^2 = 0.5480$",
            "  - Generalization Delta ($\\Delta R^2$): **0.0031**",
            "• Linear Regression (MAE):",
            "  - Train MAE = 5.02 min | Test MAE = 5.00 min",
            "• Logistic Regression (Accuracy):",
            "  - Train Acc = 81.84% | Test Acc = 81.66%",
            "  - Generalization Delta ($\\Delta \\text{Acc}$): **0.18%**"
        ],
        "Diagnostic Evaluation",
        [
            "• Overfitting (High Variance) Check: Ruled out because test metrics match training metrics without degradation.",
            "• Underfitting (High Bias) Check: Ruled out because models capture 54.8% of delivery variance and 81.7% classification accuracy across 45,593 records.",
            "• Final Diagnosis: Both models demonstrate optimal bias-variance tradeoff and robust generalization."
        ]
    )

    # -------------------------------------------------------------------------
    # SLIDE 26: Step 15 — Key Analytical Findings Summary
    # -------------------------------------------------------------------------
    slide26 = prs.slides.add_slide(blank_layout)
    add_header(slide26, "Key Analytical Findings Summary", "Step 15", "Core Insights Extracted from 45,593 Food Delivery Transactions")
    add_two_column_cards(
        slide26,
        "Demand & Temporal Insights",
        [
            "• Concentrated Demand Cycles: 65.5% of total daily demand occurs in bimodal lunch (12–14h) and dinner (18–22h) windows.",
            "• Dinner Peak Dominance: 19:00 is the peak order hour with 4,595 transactions.",
            "• Weekend Volume Expansion: Friday evening to Sunday accounts for peak weekly order density."
        ],
        "Logistical & Model Insights",
        [
            "• Severe Traffic Bottleneck: Jam conditions add an average +14 minutes delay across all order types.",
            "• High Courier Impact: Highly rated couriers with well-maintained vehicles reduce fulfillment times by ~7–9 minutes.",
            "• Predictive Reliability: Linear Regression forecasts delivery duration within 5 minutes MAE; Logistic Regression identifies peak windows with 81.7% accuracy."
        ]
    )

    # -------------------------------------------------------------------------
    # SLIDE 27: Actionable Business Recommendations
    # -------------------------------------------------------------------------
    slide27 = prs.slides.add_slide(blank_layout)
    add_header(slide27, "Actionable Business Recommendations", "Impact", "Operational Optimization Strategies for Delivery Platforms")
    add_two_column_cards(
        slide27,
        "Fleet Dispatch & Routing",
        [
            "1. Dynamic Courier Pre-Allocation: Pre-position delivery couriers in dense restaurant hubs 30 minutes prior to dinner peak (17:30).",
            "2. Smart Batching Controls: Limit concurrent multi-deliveries to a maximum of 2 stops during Jam traffic (each extra stop adds +3.44 min).",
            "3. Vehicle Maintenance Subsidies: Provide fleet maintenance rewards to couriers maintaining Tier 1/2 vehicle condition."
        ],
        "Customer Experience & Pricing",
        [
            "4. Dynamic ETA Buffers: Automatically expand customer delivery estimates by 8–12 minutes during peak traffic congestion alerts.",
            "5. Tiered Courier Incentives: Provide higher per-order bonuses during severe weather and dinner peaks to prevent rider shortages.",
            "6. Off-Peak Order Promos: Offer discount vouchers during 15:00–17:00 troughs to flatten operational demand spikes."
        ]
    )

    # -------------------------------------------------------------------------
    # SLIDE 28: Future Scope & Limitations
    # -------------------------------------------------------------------------
    slide28 = prs.slides.add_slide(blank_layout)
    add_header(slide28, "Future Scope & Project Limitations", "Future Scope", "Opportunities for Extended Analytics & Platform Scaling")
    add_two_column_cards(
        slide28,
        "Project Limitations",
        [
            "• Straight-Line Distance: Haversine distance approximates route length; actual turn-by-turn road networks may differ.",
            "• Linear Assumption: Linear Regression captures additive linear factors; non-linear traffic interactions require ensemble tree modeling."
        ],
        "Future Enhancement Avenues",
        [
            "• Live GPS Map Routing: Integrate OpenStreetMap / Google Maps Routing API for real-time turn-by-turn distance.",
            "• Non-Linear Ensemble Models: Implement Random Forest and XGBoost to model complex weather-traffic interactions.",
            "• Order Basket Analytics: Incorporate order monetary value and item quantities into dynamic kitchen prep modeling."
        ]
    )

    # -------------------------------------------------------------------------
    # SLIDE 29: References & Academic Acknowledgements
    # -------------------------------------------------------------------------
    slide29 = prs.slides.add_slide(blank_layout)
    add_header(slide29, "References & Academic Acknowledgements", "Conclusion", "TYBCA 602 DAP Examination Defense Ready")
    add_two_column_cards(
        slide29,
        "Academic References",
        [
            "• VNSGU 602 Data Analytics Using Python (DAP) Syllabus & Lab Manual.",
            "• DAP Reference Architecture: Zomato DAP Benchmark Guidelines (`stepbystep.md` & `marking-structure-scheme.md`).",
            "• Scikit-learn Documentation: Pedregosa et al., OLS Regression & Logistic Regression.",
            "• McKinney, Wes: Python for Data Analysis (Pandas, Numpy)."
        ],
        "Project Deliverables Summary",
        [
            "• 5 Academic Jupyter Notebooks (`01` to `05` in `notebooks/`).",
            "• 11 High-Resolution Generated Visualizations in `outputs/figures/`.",
            "• 2 Serialized Machine Learning Models in `outputs/models/`.",
            "• Comprehensive Documentation in `docs/` & `README.md`.",
            "\n🎓 Thank You! Open for Questions & External Viva Defense."
        ]
    )

    # Save presentation
    prs.save(OUTPUT_PPTX)
    print(f"Successfully generated PowerPoint presentation ({len(prs.slides)} slides) at:\n{OUTPUT_PPTX}")

if __name__ == '__main__':
    create_presentation()
