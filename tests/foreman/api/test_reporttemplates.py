# -*- encoding: utf-8 -*-
"""Unit tests for the ``report_templates`` paths.

:Requirement: Report templates

:CaseAutomation: Automated

:CaseLevel: Acceptance

:CaseComponent: API

:TestType: Functional

:CaseImportance: High

:Upstream: No
"""

from robottelo.datafactory import gen_string
from robottelo.decorators import tier1, tier2, stubbed
from robottelo.test import APITestCase

from nailgun import entities


class ComputeResourceTestCase(APITestCase):
    """Tests for ``katello/api/v2/report_templates``."""

    @tier1
    def test_positive_e2e_crud(self):
        """Run CRUD tests

        :id: a4b577db-144e-6751-a42e-e83887464986

        :setup: User with rights to CRUD report templates

        :steps:

            1. POST /api/report_templates
            2. GET /api/report_templates
            3. GET /api/report_templates/:id
            4. PUT /api/report_templates/:id
            5. DELETE /api/report_templates/:id

        :expectedresults: Report is deleted

        :CaseImportance: High
        """
        name = gen_string('alpha')
        new_name = gen_string('alpha')
        template = gen_string('alpha')
        # create and read report template
        entities.ReportTemplate(name=name, template=template).create()
        rt = entities.ReportTemplate().search(query={'search': 'name={0}'.format(name)})[0].read()
        self.assertEquals(name, rt.name)
        self.assertEquals(template, rt.template)
        # update report template
        entities.ReportTemplate(id=rt.id, name=new_name).update({'name'})
        rt = entities.ReportTemplate().\
            search(query={'search': 'name={0}'.format(new_name)})[0].read()
        self.assertEquals(new_name, rt.name)
        self.assertEquals(template, rt.template)
        rts = entities.ReportTemplate().search(query={'search': 'name={0}'.format(name)})
        self.assertEqual(len(rts), 0)
        # delete report template
        entities.ReportTemplate(id=rt.id).delete()
        rts = entities.ReportTemplate().search(query={'search': 'name={0}'.format(new_name)})
        self.assertEqual(len(rts), 0)

    @tier1
    @stubbed()
    def test_positive_generate_report_nofilter(self):
        """Generate Host Status report

        :id: a4b687db-144e-4761-a42e-e93887464986

        :setup: User with reporting access rights, some report template, at least two hosts

        :steps:

            1. POST /api/report_templates/:id/generate

        :expectedresults: Report is generated for all hosts visible for user

        :CaseImportance: High
        """

    @tier1
    @stubbed()
    def test_positive_generate_report_filter(self):
        """Generate Host Status report

        :id: a4b677cb-144e-4761-a42e-e93887464986

        :setup: User with reporting access rights, some report template, at least two hosts

        :steps:

            1. POST /api/report_templates/:id/generate ... # define input_values

        :expectedresults: Report is generated for the host specified by the filter

        :CaseImportance: High
        """

    @tier2
    @stubbed()
    def test_positive_report_add_userinput(self):
        """Add user input to template

        :id: a4a577db-144e-4761-a42e-e86887464986

        :setup: User with reporting access rights

        :steps:

            1. PUT /api/templates/:template_id/template_inputs/:id ... # add user input

        :expectedresults: User input is assigned to the report template

        :CaseImportance: Medium
        """

    @tier2
    @stubbed()
    def test_positive_lock_report(self):
        """Lock report template

        :id: a4c577db-144e-4761-a42e-e83887464986

        :setup: User with reporting access rights, some report template that is not locked

        :steps:

            1. PUT /api/report_templates/:id ... # report_template[locked] = true

        :expectedresults: Report is locked

        :CaseImportance: Medium
        """

    @tier2
    @stubbed()
    def test_positive_unlock_report(self):
        """Unlock report template

        :id: dae2bff8-340c-4d4c-8349-a2155507a3ab

        :setup: User with reporting and unlock access rights, some report template that is locked

        :steps:

            1. PUT /api/report_templates/:id ... # report_template[locked] = false

        :expectedresults: Report is unlocked

        :CaseImportance: Medium
        """

    @tier2
    @stubbed()
    def test_positive_export_report(self):
        """Export report template

        :id: a4b577db-144e-4761-a42e-a83887464986

        :setup: User with reporting access rights, some report template

        :steps:

            1. /api/report_templates/:id/export

        :expectedresults: Report script is shown

        :CaseImportance: Medium
        """

    @tier2
    @stubbed()
    def test_positive_clone_locked_report(self):
        """Clone locked report template

        :id: 9b77242d-31e4-4930-83dd-8bffa1d6b1df

        :setup: User with reporting access rights, some report template that is locked

        :steps:

            1. POST /api/report_templates/:id/clone

        :expectedresults: Report is cloned

        :CaseImportance: Medium
        """

    @tier2
    @stubbed()
    def test_positive_generate_report_sanitized(self):
        """Generate report template where there are values in comma outputted which might brake CSV format

        :id: a4b577db-144e-4961-a42e-e93887464986

        :setup: User with reporting access rights, Host Statuses report,
                a host with OS that has comma in its name

        :steps:

            1. POST /api/report_templates/:id/generate

        :expectedresults: Report is generated in proper CSV format (value with comma is quoted)

        :CaseImportance: Medium
        """

    @tier2
    @stubbed()
    def test_negative_create_report_without_name(self):
        """Try to create a report template with empty name

        :id: a4b577db-144e-4771-a42e-e93887464986

        :setup: User with reporting access rights

        :steps:

            1. POST /api/report_templates

        :expectedresults: Report is not created

        :CaseImportance: Medium
        """

    @tier2
    @stubbed()
    def test_negative_delete_locked_report(self):
        """Try to delete a locked report template

        :id: a4b577db-144e-4871-a42e-e93887464986

        :setup: User with reporting access rights, some report template that is locked

        :steps:

            1. DELETE /api/report_templates/:id

        :expectedresults: Report is not deleted

        :CaseImportance: Medium
        """
