Résumé
======

Currently this will install and run a small stack that includes a gunicorn server, a postgresql server, and a nagios monitoring server, all of them deployed as microservices inside Docker containers.  Vagrant support is planned, but not yet implemented.

[![Build Status](https://travis-ci.org/executive-consultants-of-los-angeles/rsum.svg?branch=master)](https://travis-ci.org/executive-consultants-of-los-angeles/rsum)

Below is the Engineering version of my CV, which highlights my skills as a Site Reliability Engineer and Python Developer.

```yaml
---
intro:
  id: 1
  name: "Alex Harris"
  position: "Python Developer / Site Reliablity Engineer"
  social_media_links:
    facebook: 'https://www.facebook.com/eclacfo'
    twitter: 'https://twitter.com/eclacfo'
    linkedin: 'https://www.linkedin.com/in/eclacfo'
    github: 'https://github.com/eclacfo'
summary:
  id: 2
  content: "Straight shooter with upper management written all over me."
  build_status:
    name: "Build Status"
    rsum:
      name: "CV"
      image:
        "https://travis-ci.org/executive-consultants-of-los-angeles/rsum.svg?branch=master"
      link:
        "https://travis-ci.org/executive-consultants-of-los-angeles/rsum"
    ngos:
      name: "Nagios"
      image:
        "https://travis-ci.org/executive-consultants-of-los-angeles/nagios.svg?branch=master"
      link:
        "https://travis-ci.org/executive-consultants-of-los-angeles/nagios"
    psql:
      name: "PostgreSQL"
      image:
        "https://travis-ci.org/executive-consultants-of-los-angeles/psql.svg?branch=master"
      link:
        "https://travis-ci.org/executive-consultants-of-los-angeles/psql"
skills:
  id: 3
  start: 2000
  infrastructure_automation:
    id: 1
    name: "Infrastructure Automation and Administration"
    start: 2000
    ansible:
      name: "Ansible"
      start: 2013
    molecule:
      name: "Molecule"
      start: 2016
    bash:
      name: "Bourne Again SHell"
      start: 2000
    vim:
      name: "Very IMproved Text Alexitor"
      start: 2000
  cloud_architecture:
    id: 2
    name: "Cloud Computing Services"
    start: 2008
    amazon_web_services:
      name: "Amazon Web Services"
      start: 2008
    microsoft_azure:
      name: "Microsoft Azure"
      start: 2016
    google_cloud:
      name: "Google Cloud"
      start: 2016
    digital_ocean:
      name: "Digital Ocean"
      start: 2014
  software_development:
    id: 3
    name: "Software Engineering"
    start: 2004
    agile:
      name: "Agile Development"
      start: 2014
    sdlc:
      name: "Software Development Life Cycle"
      start: 2000
    scm:
      name: "Source Code Management"
      start: 2006
    git:
      name: "git"
      start: 2013
    svn:
      name: "SubVersion"
      start: 2006
  linux_unix:
    id: 4
    name: "Linux Administration"
    start: 2000
    redhat:
      name: "RedHat Enterprise Linux"
      start: 2000
    debian:
      name: "Debian Linux"
      start: 2000
    ubuntu:
      name: "Ubuntu Linux"
      start: 2005
    gentoo:
      name: "Gentoo Linux"
      start: 2004
  programming:
    id: 5
    name: "Programming Languages"
    start: 2000
    python:
      name: "Python"
      start: 2014
    java:
      name: "Java"
      start: 2016
    php:
      name: "Personal Home Page"
      start: 2000
    javascript:
      name: "JavaScript"
      start: 2000
  databases:
    id: 6
    name: "Relational and Other Databases"
    start: 2000
    postgresql:
      name: "PostgreSQL"
      start: 2007
    mysql:
      name: "MySQL"
      competence: 70
      start: 2000
    mongodb:
      name: "MongoDB"
      start: 2014
values:
  id: 4
  introduction: 'A clearly defined system of ethics is vital to a
    happy and productive life, so I have defined my values as
    the following.  These are listed in order or precedence
    from left to right.'
  content:
    loyalty:
      id: 1
      col: 'class="col-md-3 col-sm-6 md-margin-b-4"'
      service: 'class="service" data-height="height"'
      icon: 'class="service-icon icon-badge"'
      text: 'One good turn deserves another, and really this
        comes down to the Golden Rule: do unto others
        and then run. But seriously, I do what I can to help
        people that have helped me and I don''t ask people for
        action that I haven''t done myself in the past.'
    industry:
      id: 2
      col: 'class="col-md-3 col-sm-6 md-margin-b-4"'
      service:
        'class="service bg-color-base wow zoomIn"
          data-height="height"
          data-wow-duration=".3"
          data-wow-delay=".1s"'
      icon: ' class="service-icon color-white icon-chemistry"'
      text: 'You know what they say about Idle Hands. . . Seth
        Green would be homeless if not for Seth McFarlane.
        But seriously, I find I can''t properly enjoy leisure
        unless it''s leisure that''s been earned.'
    efficiency:
      id: 3
      col: 'class="col-md-3 col-sm-6 sm-margin-b-4"'
      service: 'class="service" data-height="height"'
      icon: 'class="service-icon icon-screen-tablet"'
      text: 'With that said, working hard but dumb is not
        going to get you very far, so I like things that are
        speedy and free of waste.'
    wealth:
      id: 4
      col: 'class="col-md-3 col-sm-6"'
      service: 'class="service" data-height="height"'
      icon: 'class="service-icon  icon-mustache"'
      text: 'Finally, this requires some clarity.&nbsp;&nbsp;I do not mean
        money when I say wealth because the two are not synonymous.
        Wealth in this context refers to a richness of resources
        such as endurance, information, health, and kindness.
        Essentially, an ability to get things done.'
experience:
  id: 5
  introduction: 'Counting from the first time I installed
    linux onto a pc I have been actively doing some kind
    of programming or computer administration type of
    effort for more than twenty years.  I have been getting
    paid for it about fifteen of those years, not counting
    this year.'
  cfo_at_gahan_corporation:
    id: 1
    duration: "May 2016 - Present"
    location: "Los Angeles, California"
    company: "Gahan Corporation"
    position: "Chief Financial Officer"
    projects:
      technology:
        - "maintain multiple cloud services"
        - "total cost of ownership < $100/mo"
        - "pretty good uptime"
        - "at least not terrible security"
      legal:
        - "converted from an LLC started May 2016"
        - "wrote the filed Articles of Incorporation"
        - "also have an author credit on the bylaws"
        - "have written every agreement executed by the corporation so far"
        - "keep the corporation in good standing with the State of California"
      finance:
        - "aiming at issuing registered stock by 2020"
        - "pretty depressing at the moment"
        - "maintain books to GAAP standards"
        - "keep us up to date with taxes and reporting"
  abiogenix_incorporated:
    id: 2
    duration: "August 2014 - May 2017"
    location: "Los Angeles, California"
    company: "Abiogenix Incorporated"
    position: "Python Developer / Site Reliability Engineer"
    projects:
      enterprise_resource_planning:
        - "automated deployment and maintenance of the Odoo ERP system"
        - "installed Google SSO for better auditing"
      buy_my_ubox_com:
        - "designed and implemented the my-ubox.com web store"
        - "makes use of the Django web framework"
        - "some custom code that integrates the order system with Odoo"
      atlassian:
        - "deployed Atlassian suite to Abiogenix cloud assets"
        - "maintain those same tools for uptime and performance"
        - "very limited budget"
      networking:
        - "transfered my-ubox.com to Amazon's Route 53 service"
        - "transfered abiogenix.com to Amazon's Route 53 service"
  caa:
    id: 3
    duration: "September 2015  -  March 2016 (7 months)"
    location: "Los Angeles, California"
    company: "Creative Artists Agency"
    position: "Python Developer / Site Reliability Engineer"
    projects:
      jupyterhub:
        - "automated deployment of JupyterHub with Ansible"
        - "instructed analysts on the use of Python and JupyterHub"
        - "enabled the quants to transfer data from Excel to WorkDay"
      ansible_tower:
        - "refactored existing Ansible playbooks for improved security"
        - "implemented best practices in all Ansible playbooks"
        - "managed more than one upgrade of Ansible Tower server"
        - "enabled logging and monitoring with New Relic and Splunk"
      continuous_integration:
        - "project was a year late on delivery upon my assignment"
        - "walked into an unfamiliar stack and uncooperative team"
        - "within one quarter the project was delivering new features daily"
        - "enabled Behave testing and eliminated failures due to process"
        - "used Ansible Tower and Jenkins server for deployment"
  build_manager_toyota_motor_sales:
    id: 4
    duration: "April 2015  -  July 2015 (4 months)"
    location: "Los Angeles, California"
    company: "Toyota Motor Sales"
    position: "Build Manager"
    projects:
      atlassian:
        - "maintained project git repository"
        - "managed branches, pull requests, and releases"
        - "trained 22 developers on git flow branching model"
        - "created process for documentation of development"
        - "guided developers in resolution of merge conflicts"
      continuous_delivery:
        - "deployed spark and hadoop cluster for distributed processing"
        - "automated builds of all projects within the git repository"
        - "dployed and administered Jenkins server with Ansible"
  cloud_architect_toyota_motor_sales:
    id: 5
    duration: "January 2015  -  July 2015 (7 months)"
    location: "Los Angeles, California"
    company: "Toyota Motor Sales"
    position: "Site Reliability Engineer"
    projects:
      ansible:
        - "reduced deployment time by a factor of 15 with Ansible"
        - "automated deployment of all resources required by project"
        - "managed Red Hat Enterprise Linux 7 servers"
      amazon_web_services:
        - "configured and deployed all infrastructure"
        - "administered same"
        - "managed budget for aws monthly spend"
  lead_python_developer_toyota_motor_sales:
    id: 6
    duration: "December 2014  -  July 2015 (8 months)"
    location: "Los Angeles, California"
    company: "Toyota Motor Sales"
    position: "Lead Python Developer"
    projects:
      training:
        - "wrote Python style guide"
        - "implemented smart commits for JIRA issues"
        - "trained offshore developers in the use of gitflow"
      scraping:
        - "used Python, Scrapy, MongoDB, and BASH for project"
        - "scraped web for information relevant to project"
        - "identified and removed redundancies within the project"
        - "ran daily scrum meetings and maintained a storyboard"
      proposal:
        - "authored A3 to streamline build process"
  chief_technical_officer_mintspare:
    id: 7
    duration: "February 2014  -  January 2015 (1 year)"
    location: "Alameda, California"
    company: "Mintspare Incorporated"
    position: "Chief Technical Officer"
    projects:
      webmaster:
        - "developmed all Mintspare websites"
        - "used CakePHP as well as jQuery"
      systems_administrator:
        - "administrated Mintspare databases"
        - "prevented data loss and developed schemas"
        - "responsible for all Mintspare IT infrastructure"
        - "used Ansible to automate infrastructure deployment"
        - "managed load balancing using HAProxy"
  vs_media:
    id: 8
    duration: "August 2013  -  December 2013 (5 months)"
    location: "Los Angeles, California"
    company: "VS Media"
    position: "PHP Developer / Analyst"
    projects:
      analyst:
        - "collected and analyzed data on email marketing"
        - "improved performance of email servers and content"
        - "documented control flow of complex scripts"
        - "sent roughly 150,000 emails a day"
      email_administrator:
        - "implemented new elements of the email system"
        - "created such as a centralized template store"
  thrive_marketing:
    id: 9
    duration: "April 2013  -  July 2013 (4 months)"
    location: "Nashville, Tennessee"
    company: "Thrive Marketing"
    position: "PHP Developer / Systems Administrator"
    projects:
      systems_administrator:
        - "installed and configured several different Linux servers"
        - "used distributions such as Ubuntu, CentOS, and Gentoo"
        - "also maintained a number of Windows 7 workstations"
      web_developer:
        - "developed internal products for sales operations"
        - "made use of PHP, JavaScript, jQuery, JSON, REST, and SOAP"
        - "created data models for two internal software projects"
        - "documented existing and new code"
      source_code_management:
        - "implemented git and gitflow for source code control"
        - "provided training to other employees on their use"
education:
  id: 6
  name: "Broadmoor Elementary School"
  location: "Lafayette, Louisiana"
  studies: "Kindergarten Diploma, General Studies, Kindergarten"
  duration: "1988 – 1989 (1 year)"
  projects:
    tests:
      - "I have always tested well"
      - "that is how I graduated with a GPA in the 1.7 range"
      - "it was a very prestigious kindergarten"
contact:
  id: 7
  title: "Get in Touch with Alex"
  message:
    "Alex is available most weekdays after noon Pacific Time."
  location: "Los Angeles, California, United States of America"
  phone: "(424) 209-2976"
  email: "alex@ecla.solutions"
  web: "https://ecla.solutions/"
...
# vim: ft=ansible:
```

Requirements
------------

Docker Engine, or *nix, or access to a cloud provider that supports *nix.  You will also need [Ansible](https://www.ansible.com/) and Molecule for the automated deployment. 

### Installation

```bash
ansible-galaxy install executive-consultants-of-los-angeles.r-sum-
```

## Integration Graph

This is a very rough sketch of the integration system that makes sure the site stays up while updates are continuously deployed.

![Integration Graph](files/docs/continuous-integration.png)

## Schema Diagram

Diagram of the schema that is used to store data contained in the .yml files.

![Schema Diagram](files/docs/schema.png)

Example Playbook
----------------

The development machine is named `mrsum`, so you'll want to update your Ansible hosts file to reflect the following:

```yaml
[mrsums]
mrsum ansible_connection=docker
mpsql ansible_connection=docker
mngos ansible_connection=docker
```

This will allow the [Ansible Galaxy Role](https://galaxy.ansible.com/executive-consultants-of-los-angeles/rsum/)  install all of the required microservices.

The easiest way to deploy this locally is with [Molecule](https://github.com/metacloud/molecule).  You can install the latest version of [Molecule](https://github.com/metacloud/molecule) with `pip install molecule --pre`.  Once that is done, you can run the tests with `molecule test` from a BASH cli.  I only use BASH, so that's all I'm testing it on.  If you're using some other kind of shell, well, you know, good luck to you.

You oughtn't need to write your own playbook for this because the required playbooks are located in the `molecule/default/` directory, but just for the sake of discussion, it would look something like this:

```yaml
---
- name: 'converge'
  hosts: 'mrsum'
  roles:
    - role: executive-consultants-of-los-angeles.rsum
...
# vim: ft=ansible:
```

But really, if you want to see the thing running locally for whatever reason, you can run `molecule converge` to create and deploy the required Docker containers.  On occasion `molecule converge` won't actually run the required Ansible scripts and will instead only create the required Docker containers.  If you find yourself in such a situation take heed: `ansible-galaxy install -r molecule/default/requirements.yml` will install the required roles to your machine and `ansible-playbook molecule/default/playbook.yml` will execute the automated deployment. 

You'll then need to wait a bit for the deployments to finish, but when they do you should be able to see the site at `http://127.0.0.1:8192`.  The Nagios monitoring software will be up at 'http://127.0.0.1:2050/nagios3/`.  Unless it didn't start Apache, which will happen from time to time, in which case you can amend the situation by running `docker exec mngos service apache2 start` at which point you should see all of the services in the Nagios console.  The username is nagiosadmin and the password, well, you should be able to find where that is set.  If you can't, I probably don't want to be working with or for you.  So, good luck!

License
-------

Unlicense

Author Information
------------------

Written by Alex Harris for the Executive Consultants of Los Angeles. 
