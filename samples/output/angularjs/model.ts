module Just.Code
{
	export class SampleTable
	{
        id: number;
        name: string;
        cost: number;
        startedAt: Date;

		constructor(properties?: any)
		{
			for (var key in properties)
			{
				this[key] = properties[key];
			}
		}
	}
}