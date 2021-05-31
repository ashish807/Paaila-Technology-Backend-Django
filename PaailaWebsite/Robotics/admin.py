from django.contrib import admin
from .models import I_1_RoboticsPageTopContent,I_2_RoboticsPageTypeOfRobot,I_3_RoboticsPageDeployRobotsSection,I_4_RoboticsPageExpertiseSection,Z_1_TypeOfRobotPageTopContents,Z_2_TypeOfRobotPageDeployRobot,Z_3_TypeOfRobotEveryThingRobotics,Z_4_TypeOfRobotPageHowWeDoIT

# Register your models here.

admin.site.register(I_1_RoboticsPageTopContent)

class I_2_RoboticsPageTypeOfRobotAdmin(admin.ModelAdmin):
    list_display =('name_robot', 'title')
    prepopulated_fields = {'slug': ('name_robot',)}

admin.site.register(I_2_RoboticsPageTypeOfRobot,I_2_RoboticsPageTypeOfRobotAdmin)

admin.site.register(I_3_RoboticsPageDeployRobotsSection)

admin.site.register(I_4_RoboticsPageExpertiseSection)

class Z_1_TypeOfRobotPageTopContentsAdmin(admin.ModelAdmin):
    list_display=('robot_type','title')

admin.site.register(Z_1_TypeOfRobotPageTopContents,Z_1_TypeOfRobotPageTopContentsAdmin)


class Z_2_TypeOfRobotPageDeployRobotAdmin(admin.ModelAdmin):
    list_display=('robot_type','category_title')
admin.site.register(Z_2_TypeOfRobotPageDeployRobot, Z_2_TypeOfRobotPageDeployRobotAdmin)

class Z_3_TypeOfRobotEveryThingRoboticsAdmin(admin.ModelAdmin):
    list_display=('robot_type','category_title')
admin.site.register(Z_3_TypeOfRobotEveryThingRobotics, Z_3_TypeOfRobotEveryThingRoboticsAdmin)


class Z_4_TypeOfRobotPageHowWeDoITAdmin(admin.ModelAdmin):
    list_display=('robot_type','category_title')
admin.site.register(Z_4_TypeOfRobotPageHowWeDoIT, Z_4_TypeOfRobotPageHowWeDoITAdmin)

