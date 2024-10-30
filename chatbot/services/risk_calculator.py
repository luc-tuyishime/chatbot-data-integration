class RiskCalculator:
    @staticmethod
    def calculate_insurance_risk(age, lifestyle_score):
        base_risk = age / 100
        lifestyle_factor = (10 - lifestyle_score) / 10
        return (base_risk + lifestyle_factor) / 2

    @staticmethod
    def calculate_diabetes_risk(age, lifestyle_score):
        base_risk = age / 80
        lifestyle_factor = (10 - lifestyle_score) / 10
        return (base_risk + lifestyle_factor) / 2