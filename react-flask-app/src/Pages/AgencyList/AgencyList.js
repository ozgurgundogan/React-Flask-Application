import React from "react";
import "./AgencyList.css"
import DataTable from 'react-data-table-component';
import NavigatorMenu from "../NavigatorMenu/NavigatorMenu";
/**
*  table column styles
* */
const columns = [
      {
        name: "Id",
        selector: "id",
        sortable: true,
          maxWidth: "100px"
      },
      {
        name: "Title",
        selector: "title",
        sortable: true, grow:2
      },
      {
        name: "Domain",
        selector: "domain",
        sortable: true, grow:2
      },{
        name: "Address",
        selector: "address",
        sortable: true, grow:4
      },{
        name: "Latitude",
        selector: "lat",
        sortable: true,
        grow: 2
      },{
        name: "Longitude",
        selector: "lng",
        sortable: true,
        grow: 2
      },{
        name: "Registration Date",
        selector: "timestamp",
        sortable: true,
        grow: 3
      }
    ];

/**
*  Agency Listing class with pagination.
 *
* */
class AgencyList extends React.Component{

    state = {
        data: [],
        loading: false,
        totalRows: 0,
        perPage: 10,
    };

    /**
    *  The function called when page is loaded. It fetches data from backend.
     *
    * */
    async componentDidMount() {
        const { perPage } = this.state;
        this.setState({ loading: true });

        fetch('/agency-list?page=1&per_page='+perPage)
          .then(response => response.json())
          .then(response => {
              console.log(response.data);
              this.setState({
                  data : response.data,
                  totalRows: response.total,
                  loading: false,
              }) ;

          });

    }

    /**
    *  The function called when page is changed. It fetches data from backend with appropriate pagination.
     *
    * */
    handlePageChange = async page => {
        const { perPage } = this.state;

        this.setState({ loading: true });

        fetch('/agency-list?page='+page+'&per_page='+perPage)
          .then(response => response.json())
          .then(response => {
              this.setState({
                  data : response.data,
                  totalRows: response.total,
                  loading: false,
              }) ;
          });
    }

    /**
    *  The function called when the number of rows that visualized on the screen. It fetches data from backend with appropriate pagination.
     *
    * */

    handlePerRowsChange = async (perPage, page) => {
        this.setState({ loading: true });

        fetch('/agency-list?page='+page+'&per_page='+perPage)
          .then(response => response.json())
          .then(response => {
              this.setState({
                  loading: false,
                  data: response.data,
                  perPage,
              }) ;
          });


    }

    /**
    *  Rendering function. It renders the page.
     *
    * */
    render() {
        const { loading, data, totalRows } = this.state;
         return (
             <body>
                <NavigatorMenu agencylist="1"  adminloggedin="1"/>
                <div className="Tabling">
                  <div className="card">
                    <DataTable
                      title="AGENCIES"
                      columns={columns}
                      data={data}
                      progressPending={loading}
                      defaultSortField="id"
                      highlightOnHover
                      pagination
                      paginationServer
                      paginationTotalRows={totalRows}
                      onChangeRowsPerPage={this.handlePerRowsChange}
                      onChangePage={this.handlePageChange}
                    />
                  </div>
                </div>
            </body>
          );
        }
}


export default AgencyList;