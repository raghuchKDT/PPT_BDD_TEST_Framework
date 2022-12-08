from behave import fixture, then

def before_feature(context, feature):
     print("Runs Before Each Feature")

# def after_feature(context, feature):
#     print("Run After Each Feature")
#
# def before_scenario(context, scenario):
#     print("Run Before Each Scenario")

def after_scenario(context, scenario):
    print("Run After Each Scenario")
    context.driver.quit()