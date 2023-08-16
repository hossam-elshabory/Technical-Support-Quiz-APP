# questions.py
questions = [
    {
        'eng_question': "We have two types of connection (Main Wire and wall outlet)",
        'arabic_question': "وجد لدينا نوعين من التوصيل (Main Wire and wall outlet)",
        'options': ["True", "False"],
        'correct_answer': "True"
    },
    {
        'eng_question': "In CPE configuration 'VDSL' Parameters XDSL Transfer Mode Should be ?",
        'arabic_question': "ال 'VDSL' Parameters CDSL Transfer Mode في اعدادات الروتر يجب ان تكون ",
        'options': ["PPPOE", "PPP", "PTM"],
        'correct_answer': "PTM"
    },
    {
        'eng_question': "Which of the below is the responsible for translating any domain name into IP and Vice Versa",
        'arabic_question': "اي مما يلي مسؤول عن ترجمة اي domain name الي IP و العكس",
        'options': ["DNS", "NAT", "MTU"],
        'correct_answer': "DNS"
    },
    {
        'eng_question': "Which of the following is harder for hackers to break the conntection and steal the information",
        'arabic_question': "اي مما يلي من الصعب علي ال hackers قطع الاتصال و سرقة المعلومات منه؟",
        'options': ["HTTP", "HTTPS"],
        'correct_answer': "HTTPS"
    },
    {
        'eng_question': "Broad Hop is responsible for checking customer profile from out database ?",
        'arabic_question': "ال Broad Hop هي المسؤول عن التحقق من بيانات العميل في قواعد البيانات الخاصة بنا؟",
        'options': ["True", "False"],
        'correct_answer': "True"
    },
    {
        'eng_question': "Which if the below devices is responsible for assigning WAN IPS to CPEs?",
        'arabic_question': "مين من الاجهزة التحت دي مسؤول عن تعيين ال WAN IPS لاجهزة الروتر؟",
        'options': ["DSLAM", "BRAS", "RADIUS"],
        'correct_answer': "BRAS"
    },
    {
        'eng_question': "The Ethernet calbe ends with RJ",
        'arabic_question': "كبل ال Ethernet ال بينتهي ب RJ",
        'options': ["45", "11", "40"],
        'correct_answer': "45"
    },
    {
        'eng_question': "RADIUS is responsible to make sure that customer using his US & PW which are on our system & related to his line?",
        'arabic_question': "ال RADIUS هو المسؤول عن التأكد ان العميل بيستخدم ال US و ال PW الموجودة علي نظامنا والخاصة ب الخط بتاعو؟",
        'options': ["True", "False"],
        'correct_answer': "True"
    },
    {
        'eng_question': "DHCP is assigning automatic LAN IP's to the private devices, But NAT is responsible for translating the Private IP into Public IP",
        'arabic_question': "ال DHCP هو المسؤول عن تعيين LAN IP'S تلقائيا للاجهزة الخاصة, بينما ال NAT هي المسؤوله عن ترجمة و تحويل ال Private IP الي Public IP?",
        'options': ["True", "False"],
        'correct_answer': "True"
    },
    {
        'eng_question': "Device is using to split data and voice into 2 channgles",
        'arabic_question': "الجهاز المسؤول عن تقسيم ال data و ال voice الي قناتان مختلفتان؟",
        'options': ["Filter", "Spliter", "Rosetta"],
        'correct_answer': "Spliter"
    },
    {
        'eng_question': "ٍSurvey SLA is ..?",
        'arabic_question': "مدة المعاينة",
        'options': ["3 WD", "24H", "24 WH"],
        'correct_answer': "24H"
    },
    {
        'eng_question': "ٍwe can follow up on check availability request through BSS from ..",
        'arabic_question': "احنا ممكن نتابع طلب ال check availability من ال BSS ?",
        'options': ["Sitemap >> Integrated Operations >> check cpe by serial",
                    "Sitemap >> Integrated Operations >> check availability fixed",
                    "Sitemap >> Integrated Operations >>  Search availability PSTN"],
        'correct_answer': "Sitemap >> Integrated Operations >>  Search availability PSTN"
    },
    {
        'eng_question': "In Case CCA found Automatic TT (Automatic TT FV >> Customer Subscription >> OSS TDM Registration) CCA Action Will be ?",
        'arabic_question': "لو لقيت ال Automatic TT دي (Automatic TT FV >> Customer Subscription >> OSS TDM Registration) هتعمل ايه ؟",
        'options': ["Make new order", "Inform customer that someone will communicate with him within SLA 24H and in case of delay will renew SLA", "direct CST to exchange"],
        'correct_answer': "Inform customer that someone will communicate with him within SLA 24H and in case of delay will renew SLA"
    },
    {
        'eng_question': "WE Ardy 20 Quarter price includind fees is",
        'arabic_question': "باقة وي 20 الربع سنوي سعرها كام؟",
        'options': ["75 LE", "65 LE", "68.4 LE"],
        'correct_answer': "68.4 LE"
    },
    {
        'eng_question': "MSAN installation cycle SLA within 48H",
        'arabic_question': "مدة تركيب في ال MSAN 48H ?",
        'options': ["True", "False"],
        'correct_answer': "True"
    },
    {
        'eng_question': "CST want to renew his package (WE Ardy 35 Quarter), CCA will inform him to pay ... LE at least",
        'arabic_question': "هتقول للعميل يشحن بكام لو قلك عاوز يجدد باقة وي ارضي 35 ربع سنوي ؟",
        'options': ["215", "186", "122"],
        'correct_answer': "122"
    },
    {
        'eng_question': "Requested data from customer for check availability",
        'arabic_question': "المعلومات المطلوبة من العميل عشان نعملو Check availability ?",
        'options': ["Full name", "mobile + Full address", "Full name + Mobile + full address + ID number"],
        'correct_answer': "Full name + Mobile + full address + ID number"
    },
    {
        'eng_question': "Modify reason ( Customer Request ) will be done for free for..",
        'arabic_question': "كم عدد المرات المجانية للعميل لتغيير البيانات ؟",
        'options': ["all time", "two times", "one time"],
        'correct_answer': "two times"
    },
    {
        'eng_question': "CCA must choose one of those choices when he make check availability request",
        'arabic_question': "ممثل خدمة العملة لازم يخطار ايه و هو بيعمل check availability request",
        'options': ["MSAN FTTH Exchange", "FTTH Compound", "FTTH Compound \ Others\MSAN FTTH Exchange"],
        'correct_answer': "FTTH Compound \ Others\MSAN FTTH Exchange"
    },
    {
        'eng_question': "in check availability request ,, CCA can make Request by",
        'arabic_question': "في عملية ال check availability request, ممثل خدمة العملاء بيعمل الطلب ب ايه ؟",
        'options': ["National ID", "Mobil no", "Full name"],
        'correct_answer': "National ID"
    },
    {
        'eng_question': "CST can request to suspend his land line temporary",
        'arabic_question': "العميل ممكن يعمل ايقاف مؤقت للخط بتاعو ؟",
        'options': ["True", "False"],
        'correct_answer': "True"
    },
    {
        'eng_question': "CST can request to make his land line reciving only and do not pay his subscribtion fees",
        'arabic_question': "العميل ممكن يقدم طلب تحويل الخط لاستقبال فقط بدون رسوم (مجاني) ؟",
        'options': ["True", "False"],
        'correct_answer': "False"
    },
    {
        'eng_question': "Waiting service is free with WE Ardy 20",
        'arabic_question': "خدممة الانتظار مجانية مع باقة وي ارضي 20",
        'options': ["True", "False"],
        'correct_answer': "False"
    },
    {
        'eng_question': "we can move land line to another government",
        'arabic_question': "مممكن نحول الخط لمحافظة تانية ؟",
        'options': ["True", "False"],
        'correct_answer': "True"
    },
    {
        'eng_question': "CST can change his line category Through 111",
        'arabic_question': "العميل ممكن يحول نوع الخط من خلال 111",
        'options': ["True", "False"],
        'correct_answer': "False"
    },
    {
        'eng_question': "CST Can request change offering through 111",
        'arabic_question': "العميل ممكن يغيير الباقة من خلال 111",
        'options': ["True", "False"],
        'correct_answer': "True"
    },
    {
        'eng_question': "Before renewal date there is SMS sending to CST to remind him to pay his bill",
        'arabic_question': "في رسالة بتتبعت للعميل عشان تفكرو بلتجديد ؟",
        'options': ["True", "False"],
        'correct_answer': "True"
    },
    {
        'eng_question': "calling WE Mobil and Local calls are active without CST Request",
        'arabic_question': "خدمة ال WE Mobile + local Calls بيكونو شغالين من غير طلب العميل ؟",
        'options': ["True", "False"],
        'correct_answer': "True"
    },
    {
        'eng_question': "temporary suspension service Fees without VAT",
        'arabic_question': "سعر الايقاف المؤقت بدون الضريبة ؟",
        'options': ["20 LE", "30 LE", "50 LE"],
        'correct_answer': "20"
    },
    {
        'eng_question': "Recharge through Electronic machines is update within 48H",
        'arabic_question': "الشحن من خلال المكينات الاليه بيتحدث خلال 48H",
        'options': ["True", "False"],
        'correct_answer': "False"
    },
    {
        'eng_question': "SLA for new Account is",
        'arabic_question': "ال SLA الخاصة بالاشتراك الجديد هي",
        'options': ["72H", "48 WH", "3 Days"],
        'correct_answer': "48 WH"
    },
    {
        'eng_question': "We can determined port configured speed from which tool ",
        'arabic_question': "Port Configured speed نقدر نشوف منين",
        'options': ["Matrix", "OSS", "OM"],
        'correct_answer': "Matrix"
    },
    {
        'eng_question': "All Branches have same Working Hours and Days off ",
        'arabic_question': "الفروع ليها نفس مواعيد العمل والاجازات",
        'options': ["True", "False"],
        'correct_answer': "False"
    },
    {
        'eng_question': "We can check customer if Blocked or not from which tool",
        'arabic_question': "من خلال Blocked or not نقدر نشوف خط العميل",
        'options': ["Matrix", "OSS", "OM"],
        'correct_answer': "Matrix"
    },
    {
        'eng_question': "Our customers can not submit any tkt from WE APP",
        'arabic_question': "عملاء شركة WE لا يمكنهم تقديم أي شكوي من خلال WE APP",
        'options': ["True", "False"],
        'correct_answer': "False"
    },
    {
        'eng_question': "Which Tool we Can Know any another( Q ) Working Hours",
        'arabic_question': "نقدر نعرف مواعيد الاقسام الاخرى من خلال",
        'options': ["CST 360", "IVR", "Branch"],
        'correct_answer': "IVR"
    },
    {
        'eng_question': "New subscription can apply through",
        'arabic_question': "الاشتراكات الجديدة تتم من خلال",
        'options': ["Call Center Only", "Branch only", "Both of them"],
        'correct_answer': "Branch only"
    },
    {
        'eng_question': "Some Of Corporate Individual Postpaid Customers bill cycle on ?",
        'arabic_question': "نظام دورة الفاتورة الخاصة ببعض عملاء ال Corporate Individual Postpaid",
        'options': ["Day 16 from each month", "Day 1 from each month", "Day 22 from each month"],
        'correct_answer': "Day 22 from each month"
    },
    {
        'eng_question': "Which service customer can use static IP",
        'arabic_question': "ما هي الخدمة التي يستطيع العميل من خلالها استخدام ال static IP",
        'options': ["option pack", "Family Filter", "IPTV"],
        'correct_answer': "option pack"
    },
    {
        'eng_question': "One invoice postpaid corporate Customer want to make early renewal CCA action will be …?",
        'arabic_question': "عميل One invoice postpaid corporate طلب عمل تجديد مبكر للخدمة, ال CCA action will be",
        'options': [
                     "Make verification then make early renewal to CST from BSS عمل تأكيد على البيانات ثم عمل تجديد مبكر للخدمة من خلال ال BSS",
                     "Direct Customer to his SPOC توجيه العميل لمتابعة الطلب مع ال SPOC",
                     "Inform CST that he can't make early renewal + Create SR ابلاغ العميل بعدم القدرة على عمل طلب تجديد مبكر للخدمة + عمل SR"
                    ],
        'correct_answer': "Inform CST that he can't make early renewal + Create SR ابلاغ العميل بعدم القدرة على عمل طلب تجديد مبكر للخدمة + عمل SR"
    },
    {
        'eng_question': "CST call from same landline number and ask for early renewal CCA will ask CST about … To Verification ?",
        'arabic_question': "لو العميل بيتكلم من نفس رقم الارضي و بيطلب يعمل تجديد مبكر هتعمل verification ازاي ؟",
        'options': ["Full Name +  Last 3 digit of mobile number", "No Need Any Verification Rules", "last 7 digit of nation ID + Mobile Number"],
        'correct_answer': "No Need Any Verification Rules"
    },
    {
        'eng_question': "Any TT Must be Problem / Non-Om Problem when CCA choose from Additional Information ?",
        'arabic_question': "اي TT لازم تكون Problem / Non-Om Problem عند الاختيار من Additional Information",
        'options': ["True", "False"],
        'correct_answer': "False"
    },
    {
        'eng_question': "Line Problem SLA Is ….?",
        'arabic_question': "ال SLA الخاصة بمشكلة ال Line Problem هي...؟",
        'options': ["15 WD", "7 WD", "2 WD"],
        'correct_answer': "15 WD"
    },
    {
        'eng_question': "TE Problem No Technical Data means …?",
        'arabic_question': "  “TE Problem No Technical Data” تعني",
        'options': ["No Data", "No technical Data for Line In TE", "No Financial  Data for Line In TE"],
        'correct_answer': "No technical Data for Line In TE"
    },
    {
        'eng_question': "In Case Of Delay In Port Splitting Activity CCA Action Will Be…?",
        'arabic_question': "في حالة حدوث تأخير في مرحلة ال Port Splitting, يجب على ال CCA أن .....؟",
        'options': [
                    "Create TT And Inform CST SLA 48 WH",
                    "Create SR FBB Non Tech follow up--InstallationOrder--Splitting After SLA / Inform CST 48 H",
                    "Automatic TT Will Be Created"
                    ],
        'correct_answer': "Create TT And Inform CST SLA 48 WH"
    },
    {
        'eng_question': "Any SR will be Inquiry/offers except complain SR?",
        'arabic_question': "كل ال SR بتكون inquiry/offers معادا ال complains SR?",
        'options': ["True", "False"],
        'correct_answer': "True"
    },
    {
        'eng_question': "In Case WO Request and there is problem happened sub activity will be….?",
        'arabic_question': "في حالة حدوث مشكلة خلال مرحلة ال WO Request ال sub activity will be...؟",
        'options': ["Line Problem", "WO Problem", "TE Problem"],
        'correct_answer': "WO Problem"
    },
    {
        'eng_question': "Check Free Port SLA …?",
        'arabic_question': "ال SLA الخاصة بمشكلة Check free port هي....؟",
        'options': ["No Estimated Time", "1 WD", "48 H"],  
        'correct_answer': "No Estimated Time"
    },
    {
        'eng_question': "CCA Must Make TT ….. In Case No Technical Data Found On Matrix Tool After Call Back To CRM ?",
        'arabic_question': "من الضروري على ال CCA عمل TT......... في حالة عدم وجود أي بيانات فنية للعميل على ال Matrix tool بعد وصول التركيبات الي مرحلة ال Call Back To CRM..؟",
        'options': ["Create Matrix TT", "Duplicated Matrix TT", "Remove Matrix TT"],  
        'correct_answer': "Create Matrix TT"
    },
    {
        'eng_question': "To Review All created tickets CCA can choose …?",
        'arabic_question': "لمعرفة كل الشكاوي التي تم انشاءها من قبل يجب اختيار ...؟",
        'options': ["Modify Customer Information", "Creat service Request", "Trouble Ticket"],  
        'correct_answer': "Trouble Ticket"
    },

]
