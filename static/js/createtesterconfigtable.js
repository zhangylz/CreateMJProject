var testerdata = [{"deploystyle":{index:'local'}, "nodeid":{index:1},"gateport":{index:5101},"clusterport":{index:18001},},
			{"deploystyle":{index:'tester107'}, "nodeid":{index:1},"gateport":{index:5101},"clusterport":{index:18001},},
        ];
		
function deploystyleformatter(value, row, index) {
	return '<input class="form-control" maxlength="20" name="No_{index}" id="No_{index}" placeholder="helloworld" value={value} style="float:middle;width: 60px;"  readonly /input>'.format({index:index,value:value.index});
};

function noidformatter(value, row, index) {
	return '<input class="form-control" maxlength="6" name="nodeid_{index}" id="nodeid_{index}" placeholder="1" value={value} style="float:middle;width: 60px;"  /input>'.format({index:index, value:value.index});
};

function gateportformatter(value, row, index) {
	return '<input class="form-control" maxlength="6" name="gateport_{index}" id="gateport_{index}" placeholder="5101" value={value} style="float:middle;width: 60px;" /input>'.format({index:index, value:value.index});
};

function clusterportformatter(value, row, index) {
	return '<input class="form-control" maxlength="6" name="clusterport_{index}" id="clusterport_{index}" placeholder="18001" value={value} style="float:middle;width: 60px;"  /input>'.format({index:index, value:value.index});
};

function initConfigTable(obj) {
    obj.bootstrapTable({
        idField: 'name',
        showHeader:true,
        columns: [
                [
                    {
                        field: 'deploystyle',
                        title: '部署方式',
                        align: 'center',
						edit:{type:'text'},
						formatter: deploystyleformatter,
                    },
                    {
                        field: 'nodeid',
                        title: 'nodeid',
                        align: 'center',
						edit:{type:'text'},
						formatter: noidformatter,
                    },
                    {
                        field: 'gateport',
                        title: 'gate port',
                        align: 'center',
						edit:{type:'text'},
						formatter:gateportformatter,
                    },
                    {
                        field: 'clusterport',
                        title: 'cluster port',
						align: 'center',
						edit:{type:'text'},
						formatter: clusterportformatter,
                    }
                ],
            ],
        data: testerdata
    });
}


