################################################################################
# Automatically-generated file. Do not edit!
################################################################################

-include ../makefile.init

RM := rm -rf

# All of the sources participating in the build are defined here
-include sources.mk
-include subdir.mk
-include objects.mk

ifneq ($(MAKECMDGOALS),clean)
ifneq ($(strip $(C++_DEPS)),)
-include $(C++_DEPS)
endif
ifneq ($(strip $(C_DEPS)),)
-include $(C_DEPS)
endif
ifneq ($(strip $(CC_DEPS)),)
-include $(CC_DEPS)
endif
ifneq ($(strip $(CPP_DEPS)),)
-include $(CPP_DEPS)
endif
ifneq ($(strip $(CXX_DEPS)),)
-include $(CXX_DEPS)
endif
ifneq ($(strip $(C_UPPER_DEPS)),)
-include $(C_UPPER_DEPS)
endif
endif

-include ../makefile.defs

# Add inputs and outputs from these tool invocations to the build variables 

# All Target
all: CurveRatesPy.so

dependents:
	-cd /home/phcostello/git/DerivStuff/CppRate_Curve/Debug && $(MAKE) clean all

# Tool invocations
CurveRatesPy.so: $(OBJS) $(USER_OBJS) /home/phcostello/git/DerivStuff/CppRate_Curve/Debug/libCppRate_Curve.so
	@echo 'Building target: $@'
	@echo 'Invoking: GCC C++ Linker'
	g++ -L"/home/phcostello/git/DerivStuff/CppRate_Curve/Debug" -shared -o "CurveRatesPy.so" $(OBJS) $(USER_OBJS) $(LIBS)
	@echo 'Finished building target: $@'
	@echo ' '

# Other Targets
clean:
	-$(RM) $(OBJS)$(C++_DEPS)$(C_DEPS)$(CC_DEPS)$(LIBRARIES)$(CPP_DEPS)$(CXX_DEPS)$(C_UPPER_DEPS) CurveRatesPy.so
	-@echo ' '

.PHONY: all clean dependents
.SECONDARY:
/home/phcostello/git/DerivStuff/CppRate_Curve/Debug/libCppRate_Curve.so:

-include ../makefile.targets
