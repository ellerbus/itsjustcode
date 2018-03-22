
module Just.Code
{ 
	interface IRouteParams extends ng.route.IRouteParamsService
	{
        id: number;
	}

	class SampleTableDetailController
	{
		static $inject = [
            '$routeParams',
			'$location',
			'SampleTableRepository'];

		table: SampleTable = null;
		
		constructor(
			private $routeParams: IRouteParams,
			private $location: ng.ILocationService,
			private SampleTableRepository: Just.Code.SampleTableRepository)
		{
			SampleTableRepository
				.get($routeParams.id)
				.then(this.onloadingSampleTable);
		}

        private onloadingSampleTable = (data: SampleTable) => 
        {
            this.table = data;
        }
		
		save(): ng.IPromise<void>
		{
            this.SampleTableRepository
                .save(this.table)
                .then(this.onsaved);
		}

        private onsavedSampleTable = (data: SampleTable) => 
        {
            //  either overlay, redirect, or flash message
            angular.extend(this.table, data);
        }
	}
	
	angular.module('app').controller('SampleTableDetailController', SampleTableDetailController);
}