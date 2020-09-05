from selenium.webdriver.common.action_chains import ActionChains


class ReturnFlightSearchPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.FlightRouteDetails_text_css_selector = "body.flights div.showBlock div.container.domestic div.row div.flight-details div:nth-child(2)"
        self.driver.DateOfFlight_text_css_selector = "body.flights div.showBlock div.container.domestic div.row div.flight-details div.fight-details-passenger-info span.dates-ft"
        self.driver.NoOfAdultPax_text_css_selector = "body.flights div.showBlock div.container.domestic div.row div.flight-details div.fight-details-passenger-info span.passcount:nth-child(4)"
        self.driver.NoOfChildAndInfantPax_text_css_selector = "body.flights div.showBlock div.container.domestic div.row div.flight-details div.fight-details-passenger-info span.passcount:nth-child(6)"
        self.driver.ModifySearch_link_css_selector = "#modifysearch"
        self.driver.RefundableFlight_checkbox_css_selector = "#inlineCheckbox1"
        self.driver.FilterByAirline_dropdown_css_selector = "body.flights.showCookeiPolicy div.container.m-padding-removal div.dropdown.m-default-filter div.caret-holder span.caret.hidden-xs"
        self.driver.FilterByAirline_checkbox_css_selector = "body.flights.showCookeiPolicy div.container.m-padding-removal div.dropdown.m-default-filter ul.dropdown-menu.flight_airline div.checkbox"
        self.driver.DepartureTimeZone_dropdown_css_selector = "body.flights.showCookeiPolicy div.container.m-padding-removal div.col-lg-3.col-xs-12.deptime div.dropdown div.caret-holder span.hidden-xs.caret"
        self.driver.DepartureTimeZone_selector_css_selector = "#duration_0"
        self.driver.Stops_dropdown_css_selector = "body.flights.showCookeiPolicy div.container.m-padding-removal div.col-lg-2.col-xs-12.stops div.dropdown div.caret-holder span.hidden-xs.caret"
        self.driver.NoStopFlight_checkbox_css_selector = "body.flights div.showBlock div.container.domestic.main-div div.refine-search.filters.m-fliter-wrapper div.stops.filter-tab-3 ul.dropdown-menu div.checkbox-inline:nth-child(1)"
        self.driver.OneStopFlight_checkbox_css_selector = "body.flights div.showBlock div.container.domestic.main-div div.refine-search.filters.m-fliter-wrapper div.stops.filter-tab-3 ul.dropdown-menu div.checkbox-inline:nth-child(2)"
        self.driver.MoreThanOneStopFlight_checkbox_css_selector = "body.flights div.showBlock div.container.domestic.main-div div.refine-search.filters.m-fliter-wrapper div.stops.filter-tab-3 ul.dropdown-menu div.checkbox-inline:nth-child(3)"
        self.driver.ArrivalTime_dropdown_css_selector = "body.flights.showCookeiPolicy div.refine-search.filters.m-fliter-wrapper div.col-lg-3.col-xs-12.arrtime div.dropdown div.caret-holder span.hidden-xs.caret"
        self.driver.ArrivalTimeZone_selector_css_selector = "#arrival_0"
        self.driver.TripDuration_dropdown_css_selector = "body.flights.showCookeiPolicy div.refine-search.filters.m-fliter-wrapper div.col-lg-2.col-xs-12.tripdur div.dropdown div.caret-holder span.hidden-xs.caret"
        self.driver.FlightTripDurationStartPoint_link_css_selector = "body.flights.showCookeiPolicy div.refine-search.filters.m-fliter-wrapper div.col-lg-2.col-xs-12.tripdur div.dropdown.open ul.dropdown-menu span.irs-slider.from"
        self.driver.FlightTripDurationEndPoint_link_css_selector = "body.flights.showCookeiPolicy div.refine-search.filters.m-fliter-wrapper div.col-lg-2.col-xs-12.tripdur div.dropdown.open ul.dropdown-menu span.irs-slider.to"
        self.driver.FlightTripDurationStartPoint_text_css_selector = "body.flights.showCookeiPolicy div.refine-search.filters.m-fliter-wrapper div.col-lg-2.col-xs-12.tripdur div.dropdown.open ul.dropdown-menu span.irs-from"
        self.driver.FlightTripDurationEndPoint_text_css_selector = "body.flights.showCookeiPolicy div.refine-search.filters.m-fliter-wrapper div.col-lg-2.col-xs-12.tripdur div.dropdown.open ul.dropdown-menu span.irs-to"
        self.driver.Price_dropdown_css_selector = "body.flights.showCookeiPolicy div.refine-search.filters.m-fliter-wrapper div.col-lg-2.col-xs-12.price-filter div.dropdown div.caret-holder span.hidden-xs.caret"
        self.driver.FlightStartPrice_link_css_selector = "body.flights.showCookeiPolicy div.refine-search.filters.m-fliter-wrapper div.col-lg-2.col-xs-12.price-filter div.dropdown ul.dropdown-menu span.irs-slider.from"
        self.driver.FlightEndPrice_link_css_selector = "body.flights.showCookeiPolicy div.refine-search.filters.m-fliter-wrapper div.col-lg-2.col-xs-12.price-filter div.dropdown ul.dropdown-menu span.irs-slider.to"
        self.driver.FlightStartPrice_text_css_selector = "body.flights.showCookeiPolicy div.refine-search.filters.m-fliter-wrapper div.col-lg-2.col-xs-12.price-filter div.dropdown ul.dropdown-menu span.irs-from"
        self.driver.FlightEndPrice_text_css_selector = "body.flights.showCookeiPolicy div.refine-search.filters.m-fliter-wrapper div.col-lg-2.col-xs-12.price-filter div.dropdown ul.dropdown-menu span.irs-to"
        self.driver.DepartingFlightSortByDepartureTime_link_css_selector = "#DEPARTURE-MN"
        self.driver.DepartingFlightSortByStops_link_css_selector = "#STOP-NM"
        self.driver.DepartingFlightSortByArrivalTime_link_css_selector = "#ARRIVAL-NM"
        self.driver.DepartingFlightSortByDuration_link_css_selector = "#DURETION-LH"
        self.driver.DepartingFlightSortByPrice_link_css_selector = "#PRICE-HL"
        self.driver.FlightBooking_button_css_selector = "#book_tab-0"

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

    def filter_by_airline(self, airline_name):
        self.driver.find_element_by_css_selector(self.driver.FilterByAirline_dropdown_css_selector).click()
        count = self.driver.find_element_by_css_selector(self.driver.FilterByAirline_checkbox_css_selector)
        for airline in range(len(count)+1):
            if airline_name == self.driver.find_element_by_css_selector(self.driver.FilterByAirline_checkbox_css_selector + ":nth-child(" + str(airline) + ") label").text:
                self.driver.find_element_by_css_selector(self.driver.FilterByAirline_checkbox_css_selector + ":nth-child(" + str(airline) + ") label").click()
                break
        if airline_name == "Refundable":
            self.driver.find_element_by_css_selector(self.driver.RefundableFlight_checkbox_css_selector).click()

    def filter_by_departure_time_zone_for_onwards_flight(self, time_zone):
        self.driver.find_element_by_css_selector(self.driver.DepartureTimeZone_selector_css_selector).click()
        for all_time_zone in range(1, 5):
            if time_zone == self.driver.find_element_by_css_selector(self.driver.DepartureTimeZone_selector_css_selector + " div:nth-child(" + str(all_time_zone) + "span.time").text:
                self.driver.find_element_by_css_selector(self.driver.DepartureTimeZone_selector_css_selector + " div:nth-child(" + str(all_time_zone) + "span.time")
                break

    def filter_by_stops(self, stops):
        self.driver.find_element_by_css_selector(self.driver.Stops_dropdown_css_selector).click()
        if stops == 0:
            self.driver.find_element_by_css_selector(self.driver.NoStopFlight_checkbox_css_selector)
        elif stops == 1:
            self.driver.find_element_by_css_selector(self.driver.OneStopFlight_checkbox_css_selector)
        else:
            self.driver.find_element_by_css_selector(self.driver.MoreThanOneStopFlight_checkbox_css_selector)

    def filter_by_arriving_time_zone(self, time_zone):
        self.driver.find_element_by_css_selector(self.driver.ArrivalTime_dropdown_css_selector).click()
        for all_time_zone in range(1, 5):
            if time_zone == self.driver.find_element_by_css_selector(self.driver.ArrivalTimeZone_selector_css_selector + " div:nth-child(" + str(all_time_zone) + "span.time").text:
                self.driver.find_element_by_css_selector(self.driver.ArrivalTimeZone_selector_css_selector + " div:nth-child(" + str(all_time_zone) + "span.time")
                break

    def filter_by_trip_duration(self, start_time, end_time):
        self.driver.find_element_by_css_selector(self.driver.TripDuration_dropdown_css_selector).click()
        for self.driver.find_element_by_css_selector(self.driver.FlightTripDurationStartPoint_text_css_selector).text in range(start_time+1):
            ActionChains(self.driver).drag_and_drop(self.driver.find_element_by_css_selector(self.driver.FlightTripDurationStartPoint_link_css_selector), self.driver.find_element_by_css_selector(self.driver.FlightTripDurationStartPoint_text_css_selector)).perform()

        for self.driver.find_element_by_css_selector(self.driver.FlightTripDurationEndPoint_text_css_selector).text in range(end_time+1):
            ActionChains(self.driver).drag_and_drop(self.driver.find_element_by_css_selector(self.driver.FlightTripDurationEndPoint_link_css_selector), self.driver.find_element_by_css_selector(self.driver.FlightTripDurationEndPoint_text_css_selector)).perform()

    def filter_by_flight_price(self, start_price, end_price):
        self.driver.find_element_by_css_selector(self.driver.Price_dropdown_css_selector).click()
        for self.driver.find_element_by_css_selector(self.driver.FlightStartPrice_text_css_selector).text in range(start_price+1):
            ActionChains(self.driver).drag_and_drop(self.driver.find_element_by_css_selector(self.driver.FlightStartPrice_link_css_selector), self.driver.find_element_by_css_selector(self.driver.FlightStartPrice_text_css_selector)).perform()

        for self.driver.find_element_by_css_selector(self.driver.FlightStartPrice_text_css_selector).text in range(end_price+1):
            ActionChains(self.driver).drag_and_drop(self.driver.find_element_by_css_selector(self.driver.FlightEndPrice_link_css_selector), self.driver.find_element_by_css_selector(self.driver.FlightStartPrice_text_css_selector)).perform()

    def sort_by_flight_departure_time(self, order):
        if order == "ascending":
            self.driver.find_element_by_css_selector(self.driver.DepartingFlightSortByDepartureTime_link_css_selector).click()
        elif order == "descending":
            self.driver.find_element_by_css_selector(self.driver.DepartingFlightSortByDepartureTime_link_css_selector).click()
            self.driver.find_element_by_css_selector(self.driver.DepartingFlightSortByDepartureTime_link_css_selector).click()

    def sort_by_flight_stops(self, order):
        if order == "ascending":
            self.driver.find_element_by_css_selector(self.driver.DepartingFlightSortByStops_link_css_selector).click()
        elif order == "descending":
            self.driver.find_element_by_css_selector(self.driver.DepartingFlightSortByStops_link_css_selector).click()
            self.driver.find_element_by_css_selector(self.driver.DepartingFlightSortByStops_link_css_selector).click()

    def sort_by_flight_arrival_time(self, order):
        if order == "ascending":
            self.driver.find_element_by_css_selector(self.driver.DepartingFlightSortByArrivalTime_link_css_selector).click()
        elif order == "descending":
            self.driver.find_element_by_css_selector(self.driver.DepartingFlightSortByArrivalTime_link_css_selector).click()
            self.driver.find_element_by_css_selector(self.driver.DepartingFlightSortByArrivalTime_link_css_selector).click()

    def sort_by_flight_duration(self, order):
        if order == "ascending":
            self.driver.find_element_by_css_selector(self.driver.DepartingFlightSortByDuration_link_css_selector).click()
        elif order == "descending":
            self.driver.find_element_by_css_selector(self.driver.DepartingFlightSortByDuration_link_css_selector).click()
            self.driver.find_element_by_css_selector(self.driver.DepartingFlightSortByDuration_link_css_selector).click()

    def sort_by_flight_price(self, order):
        if order == "descending":
            self.driver.find_element_by_css_selector(self.driver.DepartingFlightSortByDuration_link_css_selector).click()
        elif order == "ascending":
            self.driver.find_element_by_css_selector(self.driver.DepartingFlightSortByDuration_link_css_selector).click()
            self.driver.find_element_by_css_selector(self.driver.DepartingFlightSortByDuration_link_css_selector).click()

    def flight_selection(self):
        self.driver.find_element_by_css_selector(self.driver.FlightBooking_button_css_selector).click()
