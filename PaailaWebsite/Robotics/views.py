from django.shortcuts import render
from .models import I_1_RoboticsPageTopContent, I_2_RoboticsPageTypeOfRobot, I_3_RoboticsPageDeployRobotsSection, I_4_RoboticsPageExpertiseSection, Z_1_TypeOfRobotPageTopContents, Z_2_TypeOfRobotPageDeployRobot, Z_3_TypeOfRobotEveryThingRobotics, Z_4_TypeOfRobotPageHowWeDoIT
# Create your views here.

def robotics(request):
    top_content = I_1_RoboticsPageTopContent.objects.all().first()
    robots = I_2_RoboticsPageTypeOfRobot.objects.all()
    deploys = I_3_RoboticsPageDeployRobotsSection.objects.all()
    deploy = I_3_RoboticsPageDeployRobotsSection.objects.all().first()
    experts = I_4_RoboticsPageExpertiseSection.objects.all()
    expert = I_4_RoboticsPageExpertiseSection.objects.all().first()
    context ={
        'top_content':top_content,
        'robots':robots,
        'deploys':deploys,
        'experts':experts,
        'deploy':deploy,
        'expert':expert,
    }
    return render(request, 'robotics/Robotics.html', context)


def robot(request, robot_type):
    top_content = Z_1_TypeOfRobotPageTopContents.objects.get(robot_type__slug = robot_type)
    deploys = Z_2_TypeOfRobotPageDeployRobot.objects.filter(robot_type__slug = robot_type)
    deploys_count = deploys.count() +1
    everythings= Z_3_TypeOfRobotEveryThingRobotics.objects.filter(robot_type__slug = robot_type)

    how_we_do=Z_4_TypeOfRobotPageHowWeDoIT.objects.filter(robot_type__slug = robot_type)
    how_count = how_we_do.count() + 1
    
    context ={
        'top_content':top_content,
        'deploys':deploys,
        'deploys_count':deploys_count,
        'everythings':everythings,
        'how_we_do':how_we_do,
        'how_count':how_count,

    }
    
    return render(request, 'robotics/pari.html', context)