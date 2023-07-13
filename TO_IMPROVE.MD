# Things to improve
- Models don't have mapped entities to handle complex data (Like relationships) or easier JSON serialization. This can be recommended for a real application.
- "Assign/Unassign methods" are not scalable, generic nor reusable. Associated entities should be handled at level of entity. With proper mappers this can be achieved.
- Controllers could have an abstract class with common methods.
- Repository forces fields to have an id. This can be improved to be more generic.
- Filter additional attributes in entities passed by the client.
- There is a lot of controller logic repeated. **It is ok because they can differ over time**, but an abstract class could be used to avoid code repetition in some cases.