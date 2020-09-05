from selenium.webdriver.common.action_chains import ActionChains


class ReturnFlightSearchPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.FlightRouteDetails_text_css_selector = "body.flights div.showBlock div.container.domestic div.row div.flight-details div:nth-child(2)"
        self.driver.DateOfFlight_text_css_selector = "body.flights div.showBlock div.container.domestic div.row div.flight-details div.fight-details-passenger-info span.dates-ft"
        self.driver.NoOfAdultPax_text_css_selector = "body.flights div.showBlock div.container.domestic div.row div.flight-details div.fight-details-passenger-info span.passcount:nth-child(4)"
        self.driver.NoOfChildAndInfantPax_text_css_selector = "body.flights div.showBlock div.container.domestic div.row div.flight-details div.fight-details-passenger-info span.passcount:nth-child(6)"
        self.driver.ModifySearch_link_css_selector = "#modifysearch"
        self.driver.ResetTheFlightSearch_button_xpath = "//input[@class='btn-filter-reset1']"
        self.driver.FilterByAirline_checkbox_css_selector = "body.flights div.showBlock div.container.domestic.main-div div.refine-search.filters.m-fliter-wrapper div.filter-tab-1 ul.dropdown-menu div.checkbox"
        self.driver.Refundable_checkbox_css_selector = "body.flights div.showBlock div.container.domestic.main-div div.refine-search.filters.m-fliter-wrapper div.filter-tab-1 ul.dropdown-menu div.pull-left"
        self.driver.DepartureTimeZone_selector_css_selector = "#duration_0"
        self.driver.ArrivalTimeZone_selector_css_selector = "#duration_1"
        self.driver.NoStopFlight_checkbox_css_selector = "body.flights div.showBlock div.container.domestic.main-div div.refine-search.filters.m-fliter-wrapper div.stops.filter-tab-3 ul.dropdown-menu div.checkbox-inline:nth-child(1)"
        self.driver.OneStopFlight_checkbox_css_selector = "body.flights div.showBlock div.container.domestic.main-div div.refine-search.filters.m-fliter-wrapper div.stops.filter-tab-3 ul.dropdown-menu div.checkbox-inline:nth-child(2)"
        self.driver.MoreThanOneStopFlight_checkbox_css_selector = "body.flights div.showBlock div.container.domestic.main-div div.refine-search.filters.m-fliter-wrapper div.stops.filter-tab-3 ul.dropdown-menu div.checkbox-inline:nth-child(3)"
        self.driver.OnwardsFlightLayoverStartPoint_link_css_selector = "body.flights div.showBlock div.container.domestic.main-div div.refine-search.filters.m-fliter-wrapper div.stops.filter-tab-3 ul.dropdown-menu div.lay-dur:nth-child(4) span.irs-slider.from.type_last"
        self.driver.OnwardsFlightLayoverEndPoint_link_css_selector = "body.flights div.showBlock div.container.domestic.main-div div.refine-search.filters.m-fliter-wrapper div.stops.filter-tab-3 ul.dropdown-menu div.lay-dur:nth-child(4) span.irs-slider.to"
        self.driver.OnwardsFlightLayoverStartPoint_text_css_selector = "body.flights div.showBlock div.container.domestic.main-div div.refine-search.filters.m-fliter-wrapper div.stops.filter-tab-3 ul.dropdown-menu div.lay-dur:nth-child(4) span.irs-from"
        self.driver.OnwardsFlightLayoverEndPoint_text_css_selector = "body.flights div.showBlock div.container.domestic.main-div div.refine-search.filters.m-fliter-wrapper div.stops.filter-tab-3 ul.dropdown-menu div.lay-dur:nth-child(4) span.irs-to"
        self.driver.ReturnFlightLayoverStartPoint_link_css_selector = "body.flights div.showBlock div.container.domestic.main-div div.refine-search.filters.m-fliter-wrapper div.stops.filter-tab-3 ul.dropdown-menu div.lay-dur:nth-child(5) span.irs-slider.from.type_last"
        self.driver.ReturnFlightLayoverEndPoint_link_css_selector = "body.flights div.showBlock div.container.domestic.main-div div.refine-search.filters.m-fliter-wrapper div.stops.filter-tab-3 ul.dropdown-menu div.lay-dur:nth-child(5) span.irs-slider.to"
        self.driver.ReturnFlightLayoverStartPoint_text_css_selector = "body.flights div.showBlock div.container.domestic.main-div div.refine-search.filters.m-fliter-wrapper div.stops.filter-tab-3 ul.dropdown-menu div.lay-dur:nth-child(5) span.irs-from"
        self.driver.ReturnFlightLayoverEndPoint_text_css_selector = "body.flights div.showBlock div.container.domestic.main-div div.refine-search.filters.m-fliter-wrapper div.stops.filter-tab-3 ul.dropdown-menu div.lay-dur:nth-child(5) span.irs-to"
        self.driver.OnwardsFlightTripDurationStartPoint_link_css_selector = "body.flights div.showBlock div.container.domestic.main-div div.refine-search.filters.m-fliter-wrapper div.tripdur.filter-tab-4 ul.dropdown-menu div.lay-dur:nth-child(1) span.irs-slider.from.type_last"
        self.driver.OnwardsFlightTripDurationEndPoint_link_css_selector = "body.flights div.showBlock div.container.domestic.main-div div.refine-search.filters.m-fliter-wrapper div.tripdur.filter-tab-4 ul.dropdown-menu div.lay-dur:nth-child(1) span.irs-slider.to"
        self.driver.OnwardsFlightTripDurationStartPoint_text_css_selector = "body.flights div.showBlock div.container.domestic.main-div div.refine-search.filters.m-fliter-wrapper div.tripdur.filter-tab-4 ul.dropdown-menu div.lay-dur:nth-child(1) span.irs-from"
        self.driver.OnwardsFlightTripDurationEndPoint_text_css_selector = "body.flights div.showBlock div.container.domestic.main-div div.refine-search.filters.m-fliter-wrapper div.tripdur.filter-tab-4 ul.dropdown-menu div.lay-dur:nth-child(1) span.irs-to"
        self.driver.ReturnFlightTripDurationStartPoint_link_css_selector = "body.flights div.showBlock div.container.domestic.main-div div.refine-search.filters.m-fliter-wrapper div.tripdur.filter-tab-4 ul.dropdown-menu div.lay-dur:nth-child(2) span.irs-slider.from.type_last"
        self.driver.ReturnFlightTripDurationEndPoint_link_css_selector = "body.flights div.showBlock div.container.domestic.main-div div.refine-search.filters.m-fliter-wrapper div.tripdur.filter-tab-4 ul.dropdown-menu div.lay-dur:nth-child(2) span.irs-slider.to"
        self.driver.ReturnFlightTripDurationStartPoint_text_css_selector = "body.flights div.showBlock div.container.domestic.main-div div.refine-search.filters.m-fliter-wrapper div.tripdur.filter-tab-4 ul.dropdown-menu div.lay-dur:nth-child(2) span.irs-from"
        self.driver.ReturnFlightTripDurationEndPoint_text_css_selector = "body.flights div.showBlock div.container.domestic.main-div div.refine-search.filters.m-fliter-wrapper div.tripdur.filter-tab-4 ul.dropdown-menu div.lay-dur:nth-child(2) span.irs-to"
        self.driver.OnwardFlightStartPrice_link_css_selector = "body.flights div.showBlock div.container.domestic.main-div div.refine-search.filters.m-fliter-wrapper div.price-filter.filter-tab-5 ul.dropdown-menu div.lay-dur.nobod:nth-child(2) span.irs-slider.from"
        self.driver.OnwardFlightEndPrice_link_css_selector = "body.flights div.showBlock div.container.domestic.main-div div.refine-search.filters.m-fliter-wrapper div.price-filter.filter-tab-5 ul.dropdown-menu div.lay-dur.nobod:nth-child(2) span.irs-slider.to"
        self.driver.OnwardFlightStartPrice_text_css_selector = "body.flights div.showBlock div.container.domestic.main-div div.refine-search.filters.m-fliter-wrapper div.price-filter.filter-tab-5 ul.dropdown-menu div.lay-dur.nobod:nth-child(2) span.irs-from"
        self.driver.OnwardFlightEndPrice_text_css_selector = "body.flights div.showBlock div.container.domestic.main-div div.refine-search.filters.m-fliter-wrapper div.price-filter.filter-tab-5 ul.dropdown-menu div.lay-dur.nobod:nth-child(2) span.irs-to"
        self.driver.ReturnFlightStartPrice_link_css_selector = "body.flights div.showBlock div.container.domestic.main-div div.refine-search.filters.m-fliter-wrapper div.price-filter.filter-tab-5 ul.dropdown-menu div.lay-dur.nobod:nth-child(4) span.irs-slider.from"
        self.driver.ReturnFlightEndPrice_link_css_selector = "body.flights div.showBlock div.container.domestic.main-div div.refine-search.filters.m-fliter-wrapper div.price-filter.filter-tab-5 ul.dropdown-menu div.lay-dur.nobod:nth-child(4) span.irs-slider.to"
        self.driver.ReturnFlightStartPrice_text_css_selector = "body.flights div.showBlock div.container.domestic.main-div div.refine-search.filters.m-fliter-wrapper div.price-filter.filter-tab-5 ul.dropdown-menu div.lay-dur.nobod:nth-child(4) span.irs-from"
        self.driver.ReturnFlightEndPrice_text_css_selector = "body.flights div.showBlock div.container.domestic.main-div div.refine-search.filters.m-fliter-wrapper div.price-filter.filter-tab-5 ul.dropdown-menu div.lay-dur.nobod:nth-child(4) span.irs-to"
        self.driver.DepartingFlightSortByAirline_link_css_selector = "#onwerdData div.refine-search.filters #AIR-AZ"
        self.driver.DepartingFlightSortByDepartureTime_link_css_selector = "#onwerdData div.refine-search.filters #DEPARTURE-MN"
        self.driver.DepartingFlightSortByDuration_link_css_selector = "#onwerdData div.refine-search.filters #DURETION-LH"
        self.driver.DepartingFlightSortByPrice_link_css_selector = "#onwerdData div.refine-search.filters #PRICE-HL"
        self.driver.ArrivingFlightSortByAirline_link_css_selector = "#returnData div.refine-search.filters #AIR-AZR"
        self.driver.ArrivingFlightSortByDepartureTime_link_css_selector = "#returnData div.refine-search.filters #DEPARTURE-MNR"
        self.driver.ArrivingFlightSortByDuration_link_css_selector = "#returnData div.refine-search.filters #DURETION-LHR"
        self.driver.ArrivingFlightSortByPrice_link_css_selector = "#returnData div.refine-search.filters #PRICE-HLR"
        self.driver.DepartingFlightSelection_radiobutton_css_selector = "#onr_0"
        self.driver.ArrivingFlightSelection_radiobutton_css_selector = "#rer_0"
        self.driver.FlightBooking_button_css_selector = "#book_tab"

    def flight_route_details(self):
        return self.driver.find_element_by_css_selector(self.driver.FlightRouteDetails_text_css_selector)

    def date_of_flight(self):
        return self.driver.find_element_by_css_selector(self.driver.DateOfFlight_text_css_selector)

    def number_of_adult_pax_in_booking(self):
        return self.driver.find_element_by_css_selector(self.driver.NoOfAdultPax_text_css_selector)

    def number_of_child_and_infant_pax_in_booking(self):
        return self.driver.find_element_by_css_selector(self.driver.NoOfChildAndInfantPax_text_css_selector)

    def modify_searched_flight(self):
        self.driver.find_element_by_css_selector(self.driver.ModifySearch_link_css_selector).click()

    def reset_searched_flight(self):
        self.driver.find_element_by_xpath(self.driver.ResetTheFlightSearch_button_xpath).click()

    def filter_by_airline(self, airline_name):
        count = self.driver.find_element_by_css_selector(self.driver.FilterByAirline_checkbox_css_selector)
        for airline in range(len(count)+1):
            if airline_name == self.driver.find_element_by_css_selector(self.driver.FilterByAirline_checkbox_css_selector + ":nth-child(" + str(airline) + ") label").text:
                self.driver.find_element_by_css_selector(self.driver.FilterByAirline_checkbox_css_selector + ":nth-child(" + str(airline) + ") label").click()
                break
        if airline_name == self.driver.find_element_by_css_selector(self.driver.Refundable_checkbox_css_selector + " label.checkbox-inline input").text:
            self.driver.find_element_by_css_selector(self.driver.Refundable_checkbox_css_selector).click()

    def filter_by_departure_time_zone_for_onwards_flight(self, time_zone):
        for all_time_zone in range(1, 5):
            if time_zone == self.driver.find_element_by_css_selector(self.driver.DepartureTimeZone_selector_css_selector + " div:nth-child(" + str(all_time_zone) + "span.time").text:
                self.driver.find_element_by_css_selector(self.driver.DepartureTimeZone_selector_css_selector + " div:nth-child(" + str(all_time_zone) + "span.time")
                break

    def filter_by_departure_time_zone_for_return_flight(self, time_zone):
        for all_time_zone in range(1, 5):
            if time_zone == self.driver.find_element_by_css_selector(self.driver.ArrivalTimeZone_selector_css_selector + " div:nth-child(" + str(all_time_zone) + "span.time").text:
                self.driver.find_element_by_css_selector(self.driver.DepartureTimeZone_selector_css_selector + " div:nth-child(" + str(all_time_zone) + "span.time")
                break

    def filter_by_stops(self, stops):
        if stops == 0:
            self.driver.find_element_by_css_selector(self.driver.NoStopFlight_checkbox_css_selector)
        elif stops == 1:
            self.driver.find_element_by_css_selector(self.driver.OneStopFlight_checkbox_css_selector)
        else:
            self.driver.find_element_by_css_selector(self.driver.MoreThanOneStopFlight_checkbox_css_selector)

    def filter_by_onwards_flight_layover_duration(self, start_time, end_time):
        for self.driver.find_element_by_css_selector(self.driver.OnwardsFlightLayoverStartPoint_text_css_selector).text in range(start_time+1):
            ActionChains(self.driver).drag_and_drop(self.driver.find_element_by_css_selector(self.driver.OnwardsFlightLayoverStartPoint_link_css_selector), self.driver.find_element_by_css_selector(self.driver.OnwardsFlightLayoverStartPoint_text_css_selector)).perform()

        for self.driver.find_element_by_css_selector(self.driver.OnwardsFlightLayoverEndPoint_text_css_selector).text in range(end_time+1):
            ActionChains(self.driver).drag_and_drop(self.driver.find_element_by_css_selector(self.driver.OnwardsFlightLayoverEndPoint_link_css_selector), self.driver.find_element_by_css_selector(self.driver.OnwardsFlightLayoverEndPoint_text_css_selector)).perform()

    def filter_by_return_flight_layover_duration(self, start_time, end_time):
        for self.driver.find_element_by_css_selector(self.driver.ReturnFlightLayoverStartPoint_text_css_selector).text in range(start_time+1):
            ActionChains(self.driver).drag_and_drop(self.driver.find_element_by_css_selector(self.driver.ReturnFlightLayoverStartPoint_link_css_selector), self.driver.find_element_by_css_selector(self.driver.ReturnFlightLayoverStartPoint_text_css_selector)).perform()

        for self.driver.find_element_by_css_selector(self.driver.ReturnFlightLayoverEndPoint_text_css_selector).text in range(end_time+1):
            ActionChains(self.driver).drag_and_drop(self.driver.find_element_by_css_selector(self.driver.ReturnFlightLayoverEndPoint_link_css_selector), self.driver.find_element_by_css_selector(self.driver.ReturnFlightLayoverEndPoint_text_css_selector)).perform()

    def filter_by_onwards_flight_trip_duration(self, start_time, end_time):
        for self.driver.find_element_by_css_selector(self.driver.OnwardsFlightTripDurationStartPoint_text_css_selector).text in range(start_time+1):
            ActionChains(self.driver).drag_and_drop(self.driver.find_element_by_css_selector(self.driver.OnwardsFlightTripDurationStartPoint_link_css_selector), self.driver.find_element_by_css_selector(self.driver.OnwardsFlightTripDurationStartPoint_text_css_selector)).perform()

        for self.driver.find_element_by_css_selector(self.driver.OnwardsFlightTripDurationEndPoint_text_css_selector).text in range(end_time+1):
            ActionChains(self.driver).drag_and_drop(self.driver.find_element_by_css_selector(self.driver.OnwardsFlightTripDurationEndPoint_link_css_selector), self.driver.find_element_by_css_selector(self.driver.OnwardsFlightTripDurationEndPoint_text_css_selector)).perform()

    def filter_by_return_flight_trip_duration(self, start_time, end_time):
        for self.driver.find_element_by_css_selector(self.driver.ReturnFlightTripDurationStartPoint_text_css_selector).text in range(start_time+1):
            ActionChains(self.driver).drag_and_drop(self.driver.find_element_by_css_selector(self.driver.ReturnFlightTripDurationStartPoint_link_css_selector), self.driver.find_element_by_css_selector(self.driver.ReturnFlightTripDurationStartPoint_text_css_selector)).perform()

        for self.driver.find_element_by_css_selector(self.driver.ReturnFlightTripDurationStartPoint_text_css_selector).text in range(end_time+1):
            ActionChains(self.driver).drag_and_drop(self.driver.find_element_by_css_selector(self.driver.ReturnFlightTripDurationStartPoint_link_css_selector), self.driver.find_element_by_css_selector(self.driver.ReturnFlightTripDurationStartPoint_text_css_selector)).perform()

    def filter_by_onwards_flight_price(self, start_price, end_price):
        for self.driver.find_element_by_css_selector(self.driver.OnwardFlightStartPrice_text_css_selector).text in range(start_price+1):
            ActionChains(self.driver).drag_and_drop(self.driver.find_element_by_css_selector(self.driver.OnwardFlightStartPrice_link_css_selector), self.driver.find_element_by_css_selector(self.driver.OnwardFlightStartPrice_text_css_selector)).perform()

        for self.driver.find_element_by_css_selector(self.driver.OnwardFlightStartPrice_text_css_selector).text in range(end_price+1):
            ActionChains(self.driver).drag_and_drop(self.driver.find_element_by_css_selector(self.driver.OnwardFlightEndPrice_link_css_selector), self.driver.find_element_by_css_selector(self.driver.OnwardFlightStartPrice_text_css_selector)).perform()

    def filter_by_return_flight_price(self, start_price, end_price):
        for self.driver.find_element_by_css_selector(self.driver.ReturnFlightStartPrice_text_css_selector).text in range(start_price+1):
            ActionChains(self.driver).drag_and_drop(self.driver.find_element_by_css_selector(self.driver.ReturnFlightStartPrice_link_css_selector), self.driver.find_element_by_css_selector(self.driver.ReturnFlightStartPrice_text_css_selector)).perform()

        for self.driver.find_element_by_css_selector(self.driver.ReturnFlightStartPrice_text_css_selector).text in range(end_price+1):
            ActionChains(self.driver).drag_and_drop(self.driver.find_element_by_css_selector(self.driver.ReturnFlightStartPrice_link_css_selector), self.driver.find_element_by_css_selector(self.driver.ReturnFlightStartPrice_text_css_selector)).perform()

    def sort_by_departing_flight_airline(self, order):
        if order == "ascending":
            self.driver.find_element_by_css_selector(self.driver.DepartingFlightSortByAirline_link_css_selector).click()
        elif order == "descending":
            self.driver.find_element_by_css_selector(self.driver.DepartingFlightSortByAirline_link_css_selector).click()
            self.driver.find_element_by_css_selector(self.driver.DepartingFlightSortByAirline_link_css_selector).click()

    def sort_by_departing_flight_departure_time(self, order):
        if order == "ascending":
            self.driver.find_element_by_css_selector(self.driver.DepartingFlightSortByDepartureTime_link_css_selector).click()
        elif order == "descending":
            self.driver.find_element_by_css_selector(self.driver.DepartingFlightSortByDepartureTime_link_css_selector).click()
            self.driver.find_element_by_css_selector(self.driver.DepartingFlightSortByDepartureTime_link_css_selector).click()

    def sort_by_departing_flight_fly_duration(self, order):
        if order == "ascending":
            self.driver.find_element_by_css_selector(self.driver.DepartingFlightSortByDuration_link_css_selector).click()
        elif order == "descending":
            self.driver.find_element_by_css_selector(self.driver.DepartingFlightSortByDuration_link_css_selector).click()
            self.driver.find_element_by_css_selector(self.driver.DepartingFlightSortByDuration_link_css_selector).click()

    def sort_by_departing_flight_price(self, order):
        if order == "descending":
            self.driver.find_element_by_css_selector(self.driver.DepartingFlightSortByDuration_link_css_selector).click()
        elif order == "ascending":
            self.driver.find_element_by_css_selector(self.driver.DepartingFlightSortByDuration_link_css_selector).click()
            self.driver.find_element_by_css_selector(self.driver.DepartingFlightSortByDuration_link_css_selector).click()

    def sort_by_returning_flight_airline(self, order):
        if order == "ascending":
            self.driver.find_element_by_css_selector(self.driver.ArrivingFlightSortByAirline_link_css_selector).click()
        elif order == "descending":
            self.driver.find_element_by_css_selector(self.driver.ArrivingFlightSortByAirline_link_css_selector).click()
            self.driver.find_element_by_css_selector(self.driver.ArrivingFlightSortByAirline_link_css_selector).click()

    def sort_by_returning_flight_departure_time(self, order):
        if order == "ascending":
            self.driver.find_element_by_css_selector(self.driver.ArrivingFlightSortByDepartureTime_link_css_selector).click()
        elif order == "descending":
            self.driver.find_element_by_css_selector(self.driver.ArrivingFlightSortByDepartureTime_link_css_selector).click()
            self.driver.find_element_by_css_selector(self.driver.ArrivingFlightSortByDepartureTime_link_css_selector).click()

    def sort_by_returning_flight_fly_duration(self, order):
        if order == "ascending":
            self.driver.find_element_by_css_selector(self.driver.ArrivingFlightSortByDuration_link_css_selector).click()
        elif order == "descending":
            self.driver.find_element_by_css_selector(self.driver.ArrivingFlightSortByDuration_link_css_selector).click()
            self.driver.find_element_by_css_selector(self.driver.ArrivingFlightSortByDuration_link_css_selector).click()

    def sort_by_returning_flight_price(self, order):
        if order == "descending":
            self.driver.find_element_by_css_selector(self.driver.ArrivingFlightSortByPrice_link_css_selector).click()
        elif order == "ascending":
            self.driver.find_element_by_css_selector(self.driver.ArrivingFlightSortByPrice_link_css_selector).click()
            self.driver.find_element_by_css_selector(self.driver.ArrivingFlightSortByPrice_link_css_selector).click()

    def flight_selection(self):
        self.driver.find_element_by_css_selector(self.driver.DepartingFlightSelection_radiobutton_css_selector).click()
        self.driver.find_element_by_css_selector(self.driver.ArrivingFlightSelection_radiobutton_css_selector).click()
        self.driver.find_element_by_css_selector(self.driver.FlightBooking_button_css_selector).click()
