module Just.Code
{ 
	export class SampleTableRepository
	{
		static $inject = ['$http'];

		url = 'sample/table/';
		
		constructor(private $http: ng.IHttpService)
		{
		}
		
		query(): ng.IPromise<SampleTable[]>
		{
			var url = this.url;
			
			var config: ng.IRequestShortcutConfig = { };
			
			return this.$http.get(url, config);
		}

		get(id: number): ng.IPromise<SampleTable>
		{
			var url = this.url + 'id: number';
			
			var config: ng.IRequestShortcutConfig = { 
				params: {id: number}
			};

			return this.$http.get(url, config);
		}
		
		save(table: SampleTable): ng.IPromise<SampleTable>
		{
			var url = this.url;
			
			var config: ng.IRequestShortcutConfig = {
				data: table
			};
			
			return this.$http.post(url, table, config);
		}
	}
	
	angular.module('app').service('SampleTableRepository', SampleTableRepository);
}