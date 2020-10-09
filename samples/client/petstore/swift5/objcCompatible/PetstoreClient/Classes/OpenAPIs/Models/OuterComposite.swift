//
// OuterComposite.swift
//
// Generated by openapi-generator
// https://openapi-generator.tech
//

import Foundation

@objc public class OuterComposite: NSObject, Codable {

    public var myNumber: Double?
    public var myString: String?
    public var myBoolean: Bool?
    public var myBooleanNum: NSNumber? {
        get {
            return myBoolean as NSNumber?
        }
    }

    public init(myNumber: Double? = nil, myString: String? = nil, myBoolean: Bool? = nil) {
        self.myNumber = myNumber
        self.myString = myString
        self.myBoolean = myBoolean
    }

    public enum CodingKeys: String, CodingKey, CaseIterable {
        case myNumber = "my_number"
        case myString = "my_string"
        case myBoolean = "my_boolean"
    }

}
