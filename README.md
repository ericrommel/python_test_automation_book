# Python Test Automation

This training was broken down into 9 weeks plus a last week dedicated to the final project. Each week can have one or more sections. Feel free to navigate there.


### [Topic 1](topics/01_python_basic/main_python_basics.md): Python Basics, Control Structures, and Functions in Test Scripts

### [Topic 2](topics/02_basic_data_structures/main_data_structures_for_test_data.md): Data Structures for Test Data

### [Topic 3](topics/03_file_handling_and_regex/main_file_handling_and_regex.md): File Handling and Regular Expressions in Testing

### [Topic 4](topics/04_oop_basic/main_introduction_to_oop.md): Intro to Object-Oriented Programming (OOP) for Test Automation

### [Topic 5](topics/05_module_packages_and_testing_frameworks/main_modules_packages_testing_framework.md): Python Modules, Packages, and Testing Frameworks

### [Topic 6](topics/06_api_testing/main_api_testing.md): API Testing with Python

### [Topic 7](topics/07_web_ui_testing/main_web_automation_with_playwright.md): Web Automation with Playwright

### [Topic 8](topics/08_ai_integration_basic/main_test_automation_integrating_ai.md): AI-Driven Test Automation: Integrating AI

### [Topic 9](topics/09_ai_integration_advanced/main_advanced_ai_driven_automation_techniques.md): Advanced AI-Driven Automation Techniques

### [Topic 10](topics/10_projects/main_building_a_project.md): Building a Test Automation Suite, utilizing both web and API testing


## Fork the Repo

A `fork` is a new repository that shares code and visibility settings with the original `upstream` repository. This is a good way to have your own repository and still having updates from the `upstream`. Here the basic steps to take it. Follow the references if you want to get it deeper.


### Creating your fork

1. Go to the repository to fork: https://github.com/ericrommel/python_test_automation_book
2. Fork the repository (aka make a copy)
3. From the forked repository, add the mentors as collaborators
4. Clone the fork (aka download the copy)
5. Make a git branch
6. Make your changes
7. Make your commits (aka do the work)
8. Open/Create a Pull Request pointing to your forked `main` branch (aka PR)
9. Set the mentors as reviewers
10. Expect comments to fix or approvals
11. Once your work is approved, you can merge in

### Updating your fork

The `main` code can change during the training. To get those changes into your fork, grab the `HTTPS` clone URL from the original repository (the home repository or `upstream`, not your fork) and do these commands:

```bash
$ git checkout main
$ git remote add upstream the-clone-https-url
$ git pull upstream main
$ git push origin main
```

Commands explained:
 - `git checkout main`: It is to switch to the forked `main` branch.
 - `git remote add upstream the-clone-https-url`: It helps you to create a label called `upstream` that is connected to the URL for the `main` project. This is a one-time configuration. Once done, you don't need to do it again next time.
 - `git pull upstream main`: It will bring all changes down onto your local. You're pulling the code that lives at the `upstream` URL for the `main` project.
 - `git push origin main`: It makes your fork (the `origin`) be synced up with what's on your local.

**Note:** Create a folder called `homework` for each `week` and work only on this one. This will avoid conflicts from whatever has in the `main` project.


### References

- [Working with forks](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks)
- [Your first open source contribution: a step-by-step technical guide](https://medium.com/@jenweber/your-first-open-source-contribution-a-step-by-step-technical-guide-d3aca55cc5a6)
