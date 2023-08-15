from enum import Enum


class OrderTopic(Enum):
    NONE_TOPIC = "NONE_TOPIC"
    #maths
    CALCULUS_OF_VARIATIONS = "CALCULUS_OF_VARIATIONS"                                   #вариационное исчисление
    VECTOR_TENSOR_ANALYSIS = "VECTOR_TENSOR_ANALYSIS"                                   #векторно-тензорный анализ
    COMPUTATIONAL_MATHEMATICS = "COMPUTATIONAL_MATHEMATICS"                             #вычислительная математика
    DISCRETE_MATHEMATICS = "DISCRETE_MATHEMATICS"                                       #дискретная математика
    DIFFUSIONS = "DIFFUSIONS"                                                           #диффуры
    MULTIPLE_INTEGRALS = "MULTIPLE_INTEGRALS"                                           #кратные интегралы
    MATHEMATICAL_ANALYSIS = "MATHEMATICAL_ANALYSIS"                                     #матан
    MATHEMATICAL_MODELING = "MATHEMATICAL_MODELING"                                     #мат. моделирование
    SYSTEM_ANALYSIS_AND_DECISION_MAKING = "SYSTEM_ANALYSIS_AND_DECISION_MAKING"         #системный анализ и принятие решений
    TFCP = "TFCP"                                                                       #ТФКП
    ANALYTICAL_GEOMETRY = "ANALYTICAL_GEOMETRY"                                         #аналитическая геометрия
    LINEAR_ALGEBRA = "LINEAR_ALGEBRA"                                                   #линал
    MATHEMATICAL_STATISTICS = "MATHEMATICAL_STATISTICS"                                 #матстаты
    ROWS = "ROWS"                                                                       #ряды
    PROBABILITY_THEORY = "PROBABILITY_THEORY"                                           #теорвер
    TOPOLOGY = "TOPOLOGY"                                                               #топология
    UMF = "UMF"                                                                         #УМФ
    FUNCTIONAL_ANALYSIS = "FUNCTIONAL_ANALYSIS"                                         #функан
    FUNCTIONS_OF_MULTIPLE_VARIABLES = "FUNCTIONS_OF_MULTIPLE_VARIABLES"                 #функции нескольких переменных
    OTHER_MATHS = "OTHER_MATHS"                                                         #математика другое
    #physics                       
    QUANTUM_MECHANICS = "QUANTUM_MECHANICS"                                             #квантовая механика
    MATERIALS_SCIENCE = "MATERIALS_SCIENCE"                                             #материаловедение
    METROLOGY = "METROLOGY"                                                             #метрология
    MECHANICS = "MECHANICS"                                                             #механика
    FLUID_AND_GAS_MECHANICS = "FLUID_AND_GAS_MECHANICS"                                 #механика жидкости и газа
    OPTICS = "OPTICS"                                                                   #оптика
    STRENGTH_OF_MATERIALS = "STRENGTH_OF_MATERIALS"                                     #сопромат
    THEORETICAL_MECHANICS = "THEORETICAL_MECHANICS"                                     #теормех
    ELECTRICITY = "ELECTRICITY"                                                         #электричество
    OTHER_PHYSICS = "OTHER_PHYSICS"                                                     #физика другое
    #it
    BASIC_IT = "BASIC_IT"
    C_IT = "C_IT"
    C_SHARP_IT = "C_SHARP_IT"
    C_PLUS_PLUS_IT = "C_PLUS_PLUS_IT"
    DELPHI_IT = "DELPHI_IT"
    EXCEL_IT = "EXCEL_IT"
    JAVA_IT = "JAVA_IT"
    JAVA_SCRIPT = "JAVA_SCRIPT"
    GO_IT = "GO_IT"
    MATLAB_IT = "MATLAB_IT"
    PYTHON_IT = "PYTHON_IT"
    PHP_IT = "PHP_IT"
    DATA_BASE_IT = "DATA_BASE_IT"
    LATEX_IT = "LATEX_IT"
    LAZARUS = "LAZARUS"
    PASCAL_IT = "PASCAL_IT"
    R_IT = "R_IT"
    OTHER_IT = "OTHER_IT"
    #engineering
    ENGINEERING_GRAPHICS = "ENGINEERING_GRAPHICS"                                       #инженерная графика
    DESCRIPTIVE_GEOMETRY = "DESCRIPTIVE_GEOMETRY"                                       #начертательная геометрия
    CIRCUITRY_AND_MECHATRONICS = "CIRCUITRY_AND_MECHATRONICS"                           #схемотехника и мехатроника
    THEORY_OF_MECHANISMS_AND_MACHINES = "THEORY_OF_MECHANISMS_AND_MACHINES"             #теория механизмов и машин
    TECHNOLOGY_OF_STRUCTURAL_MATERIALS = "TECHNOLOGY_OF_STRUCTURAL_MATERIALS"           #технология конструкционных материалов
    ELECTRONICS = "ELECTRONICS"                                                         #электроника
    ELECTRONIC_BOARDS_AND_COMPONENTS = "ELECTRONIC_BOARDS_AND_COMPONENTS"               #электронные платы и компоненты
    ELECTRICAL_ENGINEERING = "ELECTRICAL_ENGINEERING"                                   #электротехника
    ANALYTICAL_MECHANICS = "ANALYTICAL_MECHANICS"                                       #аналитическая механика
    MACHINES = "MACHINES"                                                               #станки
    OTHER_ENGINEERING = "OTHER_ENGINEERING"
    #economy
    LOGISTICS = "LOGISTICS"                                                             #логистика
    MACROECONOMICS = "MACROECONOMICS"                                                   #макроэкономика
    MARKETING = "MARKETING"                                                             #маркетинг
    MANAGEMENT = "MANAGEMENT"                                                           #менеджмент
    MICROECONOMICS = "MICROECONOMICS"                                                   #микроэкономика
    TAXATION = "TAXATION"                                                               #налогообложение
    PERSONNEL_MANAGEMENT = "PERSONNEL_MANAGEMENT"                                       #управление персоналом
    ECONOMY = "ECONOMY"                                                                 #экономика
    ACCOUNTING = "ACCOUNTING"                                                           #бухгалтерский учет
    ECONOMETRICS = "ECONOMETRICS"                                                       #эконометрика
    OTHER_ECONOMY = "OTHER_ECONOMY"                                                     #другое
    #chemistry
    ORGANIC_CHEMISTRY = "ORGANIC_CHEMISTRY"                                             #органическая химия
    ANALYTICAL_CHEMISTRY = "ANALYTICAL_CHEMISTRY"                                       #аналитическая химия
    GENERAL_CHEMISTRY = "GENERAL_CHEMISTRY"                                             #общая химия
    BIOCHEMISTRY = "BIOCHEMISTRY"                                                       #биохимия
    PHYSICAL_CHEMISTRY = "PHYSICAL_CHEMISTRY"                                           #физическая химия
    INORGANIC_CHEMISTRY = "INORGANIC_CHEMISTRY"                                         #неорганическая химия
    OTHER_CHEMISTRY = "OTHER_CHEMISTRY"                                                 #химия другое
    #languages
    RUSSIAN = "RUSSIAN"
    CHINESE = "CHINESE"
    ENGLISH = "ENGLISH"
    FRENCH = "FRENCH"
    GERMAN = "GERMAN"
    SPANISH = "SPANISH"
    OTHER_LANGUAGES = "OTHER_LANGUAGES"
    #biology
    ANATOMY = "ANATOMY"                                                                 #анатомия
    PARASITOLOGY = "PARASITOLOGY"                                                       #паразитология
    BIOINFORMATICS = "BIOINFORMATICS"                                                   #биоинформатика
    MICROBIOLOGY = "MICROBIOLOGY"                                                       #микробиология
    BOTANY = "BOTANY"                                                                   #ботаника
    MOLECULAR_BIOLOGY = "MOLECULAR_BIOLOGY"                                             #молекулярная биология
    ZOOLOGY = "ZOOLOGY"                                                                 #зоология
    GENETICS = "GENETICS"                                                               #генетика
    VIROLOGY = "VIROLOGY"                                                               #вирусология
    OTHER_BIOLOGY = "OTHER_BIOLOGY"
    #geography
    GEOGRAPHY = "GEOGRAPHY"
    #humanitarian
    HISTORY = "HISTORY"                                                                 #история
    DESIGN = "DESIGN"                                                                   #дизайн
    OBZH = "OBZH"                                                                       #ОБЖ
    PHILOSOPHY = "PHILOSOPHY"                                                           #философия
    LAW = "LAW"                                                                         #право
    OTHER_HUMANITARIAN = "OTHER_HUMANITARIAN"
    #registration
    REGISTRATION = "REGISTRATION"                                                       #оформление




ORDER_TOPIC = {"NONE_TOPIC": OrderTopic.NONE_TOPIC,
                "CALCULUS_OF_VARIATIONS": OrderTopic.CALCULUS_OF_VARIATIONS,
                "VECTOR_TENSOR_ANALYSIS": OrderTopic.VECTOR_TENSOR_ANALYSIS,
                "COMPUTATIONAL_MATHEMATICS": OrderTopic.COMPUTATIONAL_MATHEMATICS,
                "DISCRETE_MATHEMATICS": OrderTopic.DISCRETE_MATHEMATICS,
                "DIFFUSIONS": OrderTopic.DIFFUSIONS,
                "MULTIPLE_INTEGRALS": OrderTopic.MULTIPLE_INTEGRALS,
                "MATHEMATICAL_ANALYSIS": OrderTopic.MATHEMATICAL_ANALYSIS,
                "MATHEMATICAL_MODELING": OrderTopic.MATHEMATICAL_MODELING,
                "SYSTEM_ANALYSIS_AND_DECISION_MAKING": OrderTopic.SYSTEM_ANALYSIS_AND_DECISION_MAKING,
                "TFCP": OrderTopic.TFCP,
                "ANALYTICAL_GEOMETRY": OrderTopic.ANALYTICAL_GEOMETRY,
                "LINEAR_ALGEBRA": OrderTopic.LINEAR_ALGEBRA,
                "MATHEMATICAL_STATISTICS": OrderTopic.MATHEMATICAL_STATISTICS,
                "ROWS": OrderTopic.ROWS,
                "PROBABILITY_THEORY": OrderTopic.PROBABILITY_THEORY,
                "TOPOLOGY": OrderTopic.TOPOLOGY,
                "UMF": OrderTopic.UMF,
                "FUNCTIONAL_ANALYSIS": OrderTopic.FUNCTIONAL_ANALYSIS,
                "FUNCTIONS_OF_MULTIPLE_VARIABLES": OrderTopic.FUNCTIONS_OF_MULTIPLE_VARIABLES,
                "OTHER_MATHS": OrderTopic.OTHER_MATHS,
                "QUANTUM_MECHANICS": OrderTopic.QUANTUM_MECHANICS,
                "MATERIALS_SCIENCE": OrderTopic.MATERIALS_SCIENCE,
                "METROLOGY": OrderTopic.METROLOGY,
                "MECHANICS": OrderTopic.MECHANICS,
                "FLUID_AND_GAS_MECHANICS": OrderTopic.FLUID_AND_GAS_MECHANICS,
                "OPTICS": OrderTopic.OPTICS,
                "STRENGTH_OF_MATERIALS": OrderTopic.STRENGTH_OF_MATERIALS,
                "THEORETICAL_MECHANICS": OrderTopic.THEORETICAL_MECHANICS,
                "ELECTRICITY": OrderTopic.ELECTRICITY,
                "OTHER_PHYSICS": OrderTopic.OTHER_PHYSICS,
                "BASIC_IT": OrderTopic.BASIC_IT,
                "C_IT": OrderTopic.C_IT,
                "C_SHARP_IT": OrderTopic.C_SHARP_IT,
                "C_PLUS_PLUS_IT": OrderTopic.C_PLUS_PLUS_IT,
                "DELPHI_IT": OrderTopic.DELPHI_IT,
                "EXCEL_IT": OrderTopic.EXCEL_IT,
                "JAVA_IT": OrderTopic.JAVA_IT,
                "JAVA_SCRIPT": OrderTopic.JAVA_SCRIPT,
                "GO_IT": OrderTopic.GO_IT,
                "MATLAB_IT": OrderTopic.MATLAB_IT,
                "PYTHON_IT": OrderTopic.PYTHON_IT,
                "PHP_IT": OrderTopic.PHP_IT,
                "DATA_BASE_IT": OrderTopic.DATA_BASE_IT,
                "LATEX_IT": OrderTopic.LATEX_IT,
                "LAZARUS": OrderTopic.LAZARUS,
                "PASCAL_IT": OrderTopic.PASCAL_IT,
                "R_IT": OrderTopic.R_IT,
                "OTHER_IT": OrderTopic.OTHER_IT,
                "ENGINEERING_GRAPHICS": OrderTopic.ENGINEERING_GRAPHICS,
                "DESCRIPTIVE_GEOMETRY": OrderTopic.DESCRIPTIVE_GEOMETRY,
                "CIRCUITRY_AND_MECHATRONICS": OrderTopic.CIRCUITRY_AND_MECHATRONICS,
                "THEORY_OF_MECHANISMS_AND_MACHINES": OrderTopic.THEORY_OF_MECHANISMS_AND_MACHINES,
                "TECHNOLOGY_OF_STRUCTURAL_MATERIALS": OrderTopic.TECHNOLOGY_OF_STRUCTURAL_MATERIALS,
                "ELECTRONICS": OrderTopic.ELECTRONICS,
                "ELECTRONIC_BOARDS_AND_COMPONENTS": OrderTopic.ELECTRONIC_BOARDS_AND_COMPONENTS,
                "ELECTRICAL_ENGINEERING": OrderTopic.ELECTRICAL_ENGINEERING,
                "ANALYTICAL_MECHANICS": OrderTopic.ANALYTICAL_MECHANICS,
                "MACHINES": OrderTopic.MACHINES,
                "OTHER_ENGINEERING": OrderTopic.OTHER_ENGINEERING,
                "LOGISTICS": OrderTopic.LOGISTICS,
                "MACROECONOMICS": OrderTopic.MACROECONOMICS,
                "MARKETING": OrderTopic.MARKETING,
                "MANAGEMENT": OrderTopic.MANAGEMENT,
                "MICROECONOMICS": OrderTopic.MICROECONOMICS,
                "TAXATION": OrderTopic.TAXATION,
                "PERSONNEL_MANAGEMENT": OrderTopic.PERSONNEL_MANAGEMENT,
                "ECONOMY": OrderTopic.ECONOMY,
                "ACCOUNTING": OrderTopic.ACCOUNTING,
                "ECONOMETRICS": OrderTopic.ECONOMETRICS,
                "OTHER_ECONOMY": OrderTopic.OTHER_ECONOMY,
                "ORGANIC_CHEMISTRY": OrderTopic.ORGANIC_CHEMISTRY,
                "ANALYTICAL_CHEMISTRY": OrderTopic.ANALYTICAL_CHEMISTRY,
                "GENERAL_CHEMISTRY": OrderTopic.GENERAL_CHEMISTRY,
                "BIOCHEMISTRY": OrderTopic.BIOCHEMISTRY,
                "PHYSICAL_CHEMISTRY": OrderTopic.PHYSICAL_CHEMISTRY,
                "INORGANIC_CHEMISTRY": OrderTopic.INORGANIC_CHEMISTRY,
                "OTHER_CHEMISTRY": OrderTopic.OTHER_CHEMISTRY,
                "RUSSIAN": OrderTopic.RUSSIAN,
                "CHINESE": OrderTopic.CHINESE,
                "ENGLISH": OrderTopic.ENGLISH,
                "FRENCH": OrderTopic.FRENCH,
                "GERMAN": OrderTopic.GERMAN,
                "SPANISH": OrderTopic.SPANISH,
                "OTHER_LANGUAGES": OrderTopic.OTHER_LANGUAGES,
                "ANATOMY": OrderTopic.ANATOMY,
                "PARASITOLOGY": OrderTopic.PARASITOLOGY,
                "BIOINFORMATICS": OrderTopic.BIOINFORMATICS,
                "MICROBIOLOGY": OrderTopic.MICROBIOLOGY,
                "BOTANY": OrderTopic.BOTANY,
                "MOLECULAR_BIOLOGY": OrderTopic.MOLECULAR_BIOLOGY,
                "ZOOLOGY": OrderTopic.ZOOLOGY,
                "GENETICS": OrderTopic.GENETICS,
                "VIROLOGY": OrderTopic.VIROLOGY,
                "OTHER_BIOLOGY": OrderTopic.OTHER_BIOLOGY,
                "GEOGRAPHY": OrderTopic.GEOGRAPHY,
                "HISTORY": OrderTopic.HISTORY,
                "DESIGN": OrderTopic.DESIGN,
                "OBZH": OrderTopic.OBZH,
                "PHILOSOPHY": OrderTopic.PHILOSOPHY,
                "LAW": OrderTopic.LAW,
                "OTHER_HUMANITARIAN": OrderTopic.OTHER_HUMANITARIAN,
                "REGISTRATION": OrderTopic.REGISTRATION}