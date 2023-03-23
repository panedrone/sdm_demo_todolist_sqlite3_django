"""
Code generated by a tool. DO NOT EDIT.
https://sqldalmaker.sourceforge.net/
"""

from dal.project import Project
from dal.project_li import ProjectLi


class _ProjectsDao:

    def __init__(self, ds):
        self.ds = ds

    def create_project(self, p):
        """
        (C)RUD: projects
        Generated values are passed to DTO.
        :param p: Project
        :return: None
        :raises Exception: if no rows inserted.
        """
        self.ds.create_one(p)

    def read_project(self, p_id):
        """
        C(R)UD: projects
        :param p_id: int
        :return: Project
        :raises Exception: if amount of returned rows != 1.
        """
        return self.ds.read_one(Project, {'p_id': p_id})

    def delete_project(self, p_id):
        """
        CRU(D): projects
        :param p_id: int
        :return: int (the number of affected rows)
        """
        return self.ds.delete_one(Project, {'p_id': p_id})

    def get_projects(self):
        """
        :return: list[ProjectLi]
        """
        sql = """select p.*, 
                (select count(*) from tasks where p_id=p.p_id) as p_tasks_count 
                from projects p 
                order by p.p_id"""
        _res = []

        def _map_cb(row):
            _obj = ProjectLi()
            _obj.p_id = row["p_id"]  # q <- q
            _obj.p_name = row["p_name"]  # q <- q
            _obj.p_tasks_count = row["p_tasks_count"]  # q <- q
            _res.append(_obj)

        self.ds.query_all_rows(sql, [], _map_cb)
        return _res