from pydantic import BaseModel, Field, EmailStr, field_validator, computed_field, model_validator
from typing import Annotated, Literal, Optional

class Patient(BaseModel):
    
    name : Annotated[str, Field(..., min_length=5, description="Enter the name of Patient.")]
    age : Annotated[int, Field(..., gt=0, description="Enter the age of Patient")]
    gender : Annotated [Literal["Male", "Female", "Others"], Field(..., description="Gender")]
    email_address : Annotated [EmailStr, Field(...,description="Enter valid emali addess" )]
    on_panel: Annotated[bool, Field(...,description="Select True or False")]
    
    
    @model_validator(mode="after")
    def validate_on_panel(cls, model):
        if model.age < 10 and model.on_panel == True:
            raise ValueError("10 years or younger should not be on Panel")
        else:
            return model
    
    @field_validator('email_address')
    @classmethod
    def email_validator(cls, value):
        
        f_email = value.split("@")[-1]
        valid_domains=["abc.com","xyz.com"]
        
        if f_email in valid_domains:
            return value
        else:
            raise ValueError("Enter email of valid domians")
        
    @computed_field
    @property
    def cal_bmi(self) -> float:
        bmi = self.age*2
        return bmi
    
    
class PatientUpdate(BaseModel):
    
    name : Annotated[Optional[str], Field(default=None)]
    age : Annotated[Optional[int], Field(default=None)]
    gender : Annotated [Optional[Literal["Male", "Female", "Others"]], Field(default=None)]
    email_address : Annotated [Optional[EmailStr], Field(default=None)]
    on_panel: Annotated[Optional[bool], Field(default=None)]
    
    