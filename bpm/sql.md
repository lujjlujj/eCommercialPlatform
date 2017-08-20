##Search Snapshot
Select proc.app,
       proc.SNAPSHOT,
       proc.name,
       proc_item.step,
       proc_item.TYPE,
       proc_item.save_exec_context
From (Select pj.anme      as app,
             ss.anme      as SNAPSHOT,
             p.process_id as PROCESS_ID,
             p.name
      From lsw_process p
            join lsw_po_versions ver
                ON p.version_id = ver.version_summary_id
            join lsw_branch branch
                ON ver.branch_id = branch.branch_id
            join lsw_snapshot ss
                ON ss.snapshot_id = branch.tip_snapshot_id
            join lsw_project pj
                ON branch.project_id = pj.project_id) proc
      join (SELECT pj.name      as app,
                   ss.name      as SNAPSHOT,
                   a.process_id as PROCOSS_ID,
                   a.name       as step,
                   a.twcomponent_name as TYPE,
                   a.save_exec_context
            FROM lsw_process_item a
                 join lsw_po_versions ver
                    ON a.version_id = ver.version_summary_id
                 join lsw_branch branch
                    ON ver.branch_id = branch.branch_id
                 join lsw_snapshot ss
                    ON ss.snapshot_id = branch.tip_snapshot_id
                 join lsw_project pj
                    ON branch.project_id = pj.project_id
             WHERE a.save_exec_context = 'T'
                   AND a.twcomponent_name NOT IN ('ExitPoint', 'Coach', 'CoachNG', 'PostponeAction', 'SubProcess')
                   AND pj.name NOT IN ('System Data' , 'Process Portal', 'Saved Search Admin')) proc_item
       ON proc.app = proc_item.app
       AND proc.SNAPSHOT = proc_item.SNAPSHOT
       AND proc.process_id = proc_item.process_id
  ORDER BY proc.app, proc.SNAPSHOT;

##SQL to check the task lost issue
select * from lsw_bdp_instance bpd where bpd.execution_status = 1
and
(select count(*) from lsw_task lt where lt.BPD_INSTANCE_ID = bpd.BPD_INSTANCE_ID and close_datetime is null) = 0
and
(select count(*) from lsw_task lt where lt.BPD_INSTANCE_ID = bpd.BPD_INSTANCE_ID and status = 32) > 0
and
(select count(*) from LSW_INST_MSG_EXCL ex where ex.BPD_INSTANCE_ID = bpd.BPD_INSTANCE_ID) = 0
and
(select count(*) from LSW_INST_MSG_INCL incl where incl.BPD_INSTANCE_ID = bpd.BPD_INSTANCE_ID) = 0;

