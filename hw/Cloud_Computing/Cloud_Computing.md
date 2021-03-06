# 作业10

@author huhu

## 1. 简述云计算的目标和主要特点

- 背景

    计算模式变革有两大根本目标：更强大的计算能力；更方便快捷的使用方式。所以，**在提供更强大计算能力的同时，提供更加方便快捷的使用方式，是贯穿整个计算技术发展的主线**。

    云计算是计算系统后端处理能力的拓展，为**快速有效处理大量物理世界的信息提供有效的计算手段和计算能力**。



- 目标

    云计算的一个重要目标是，**把计算能力变成像水电等公用服务一样，随用随取，按需使用**。故此也有人把云计算称为 “Utility Computing”，即 **“公用服务计算”** 。云计算概念和技术，让计算成为像水电一样公共服务，便于资源共享，以及提供超大的计算能力。



- 特点

    云计算主要有7个特点：**超大规模 虚拟化 高可靠性 通用性 高可伸缩性 按需服务 极其廉价**

    同时有以下优点：

    + 透明的云端计算服务
    + “无限”多的计算资源，提供强大的计算能力
    + 按需分配，弹性伸缩，取用方便，成本低廉
    + 资源共享，降低企业IT基础设施建设维护费用
    + 应用部署快速而容易
    + 软件/应用功能更新方便快捷
    + 节省能源，绿色环保
    + 集计算技术之大成，具有很强的技术性、工程型特点




## 2. 云计算按照服务层面分类，可以分为哪三类？简述每一类的作用和特点。

按云计算服务层面进行分类：基础设施即服务（IaaS）、平台即服务（PaaS）和软件即服务（SaaS），三者从通用到专用递进。

1. 将基础设施作为服务 IaaS（Infrastructure as a Service）

   **将硬件设备等基础资源封装成服务供用户使用。**

   IaaS是把**数据中心、基础设施等硬件资源**通过Web分配给用户的商业模式，消费者通过Internet可以**从完善的计算机基础设施获得服务**。

   例如：Amazon EC2/S3

    Amazon EC2提供了一种IaaS类型的云计算服务平台，在该平台上用户可部署自己的系统软件，完成应用软件的开发和发布。

2. 将平台作为服务 PaaS（Platform as a Service）

   **对资源的抽象层次更进一步，提供用户应用程序运行环境。**

   PaaS服务使得软件开发人员**可以不购买服务器等设备环境的情况下开发新的应用程序。**

   例如：Google App Engine, Microsoft Windows Azure

    Google App Engine 提供了一种PaaS类型的云计算服务平台，用户可租用该平台的计算资源，并使用App Engine 提供的各种应用开发和支撑软件平台开发和部署自己的应用软件

3. 将软件作为服务 SaaS（Software as a Service）

   **针对性更强，它将某些特定应用软件功能封装成服务**。

   通过Internet提供软件的模式，**用户无需购买软件，而是向提供商租用基于Web的软件**，来管理企业经营活动。SaaS模式大大降低了软件，尤其是大型软件的使用成本，并且由于软件是托管在服务商的服务器上，**减少了客户的管理维护成本，可靠性也更高**。

   例如：Salesforce online CRM, 腾讯云词典

   ​


## 3. 简述怎样才算是云计算系统？

一个计算系统必须具备以下两个特征才能算是云计算系统：

1. **资源虚拟化和弹性调度**解决**小粒度**应用资源共享

   基于虚拟化和弹性调度，以按需分配方式，为小粒度应用提供计算资源，实现资源共享

2. **大数据存储处理和并行计算服务**提供**大粒度**应用计算能力

   基于云端的强大而廉价的计算能力，为大粒度应用提供传统计算系统或用户终端所无法完成的计算服务。这些计算能力包括海量数据存储能力、以及大规模并行计算能力。

   ​


## 4. 实现云计算需要构建哪四层？简述每一层的作用。

云计算系统自下而上分为：物理资源层、资源池层、管理中间件层、SOA构建层

1. **物理资源层**

   计算机、存储器、网络设施、数据库和软件等

2. **资源池层**

   将大量相同类型的资源构成同构或接近同构的资源池，如：计算资源池、存储资源池、网络资源池、数据资源池、软件资源池等。

3. **管理中间件层**

   云计算的资源管理，并对众多应用任务进行调度，使资源能够高效、安全地为应用提供服务。管理中间件层和资源池层是云计算技术的最关键部分。

   3.1 **资源管理**

   均衡使用云资源节点，检测节点故障并试图恢复或屏蔽之，并对资源的使用情况进行监视统计。包括完成负载均衡、故障检测、故障恢复、监视统计等。

   3.2 **任务管理**

   执行用户或应用提交的任务，包括完成用户任务映象（Image）的部署和管理、任务调度、任务执行、任务生命期管理等。

   3.3 **用户管理**

   ​实现云计算商业模式的一个必不可少的环节，包括提供用户交互接口、管理和识别用户身份、创建用户程序的执行环境、对用户的使用进行计费等

   3.4 **安全管理**

   保障云计算设施的整体安全，包括身份认证、访问授权、综合防护和安全审计等

4. **SOA构建层**

   Service-Oriented Architecture，面向服务的架构，封装云计算能力成标准的Web Services服务，并纳入到SOA体系。SOA构建层的功能更多依靠外部设施提供。