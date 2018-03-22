module Just.Code
{ 
	class SampleTableListController
	{
		static $inject = ['SampleTableRepository'];

		tables: SampleTable[] = null;
		
		constructor(private SampleTableRepository: Just.Code.SampleTableRepository)
		{
			SampleTableRepository
				.query()
				.then(this.onloadingSampleTables);
		}

        private onloadingSampleTables = (data: SampleTable[]) =>
        {
            this.tables = data;
        }
	}
	
	angular.module('app').controller('SampleTableListController', SampleTableListController);
}